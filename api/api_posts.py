from flask import Blueprint, request, jsonify
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import (
    create_access_token,
    jwt_optional,
    jwt_required,
    get_jwt_identity
)

from models import Post, Comment
from serializers import (
    PostIndexSchema, 
    PostSchema, PostsSchema, 
    CommentSchema, CommentsSchema
)

from pprint import pprint

blueprint = Blueprint('api_posts', __name__)


@blueprint.route('/', methods=['GET'])
@jwt_required
@marshal_with(PostsSchema(many=True))
def index():

    page = request.args.get('page', type=int, default=1)
    per_page = request.args.get('per_page', type=int, default=15)

    posts = Post.with_('user', 'comments.user').order_by('created_at', 'desc').paginate(per_page, page)

    return posts

@blueprint.route('/', methods=['POST'])
@jwt_required
@marshal_with(PostSchema())
def create():

    user_id = get_jwt_identity()
    title = request.json.get('title')
    body = request.json.get('body')

    post = Post()
    post.user_id = user_id
    post.title = title
    post.body = body
    post.save()

    return post


@blueprint.route('/<int:id>', methods=['GET'])
@jwt_optional
@marshal_with(PostSchema())
def show(id):
    post = Post.with_('user', 'attachments', 'comments.user').find_or_fail(id)
    return post


@blueprint.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required
@marshal_with(PostSchema())
def update(id):

    user_id = get_jwt_identity()
    title = request.json.get('title')
    body = request.json.get('body')

    post = Post.with_('user').where('user_id', user_id).find_or_fail(id)
    post.title = title
    post.body = body
    post.save()
    
    return post


@blueprint.route('/<int:id>', methods=['DELETE'])
@jwt_required
def destroy(id):

    user_id = get_jwt_identity()
    post = Post.where('user_id', user_id).find_or_fail(id)
    post.delete()
    return jsonify({'status': 200, 'data': None})


@blueprint.route('/<int:id>/comments', methods=['POST'])
@jwt_required
@marshal_with(PostSchema())
def comments_create(id):

    comment = Comment()
    comment.commentable_id = id
    comment.commentable_type = 'posts'
    comment.user_id = get_jwt_identity()
    comment.body = request.json.get('body')
    comment.save()

    post = Post.find(id)
    post.comments_count = post.comments_count + 1
    post.save()

    return post


@blueprint.route('/<int:id>/comments/<int:comment_id>', methods=['DELETE'])
@jwt_required
@marshal_with(PostSchema())
def comments_destroy(id, comment_id):

    Comment.destroy(comment_id)

    post = Post.find_or_fail(id)
    post.comments_count = 0 if post.comments_count - 1 < 0 else post.comments_count -1
    post.save()

    return post