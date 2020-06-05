import os
from datetime import datetime
from flask import Blueprint, session, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename
from forms import PostForm
from models import Post, Comment, Attachment

blueprint = Blueprint('posts', __name__)

UPLOAD_DIR = '/workspace/flask_orator'


@blueprint.route('/', methods=['GET'])
def index():

    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 15)

    posts = Post.with_('user', 'attachment').order_by('id', 'desc').paginate(per_page, page)

    return render_template('posts/list.html', posts=posts)


@blueprint.route('/create', methods=['GET', 'POST'])
def create():

    if not 'auth' in session:
        return redirect(url_for('users.login', redirect_url=request.url))

    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():

        post = Post()
        post.user_id = session['auth']['id']
        post.title = form.title.data
        post.body = form.body.data
        post.save()

        if form.attachments.data:
            now = datetime.now().strftime('%Y%m')
            filename = secure_filename(form.attachments.data.filename)
            # upload directory create
            directory = '{0}/static/attachments/{1}'.format(UPLOAD_DIR, now)
            if not os.path.exists(directory):
                os.mkdir(directory)
            path = os.path.join(directory, filename)
            form.attachments.data.save(path)

            attachment = Attachment()
            attachment.attachment_type = 'posts'
            attachment.attachment_id = post.id
            attachment.url = path.replace(UPLOAD_DIR, '')
            attachment.user_id = session['auth']['id']
            attachment.save()

        return redirect(url_for('posts.index'))

    return render_template('posts/form.html', form=form)


@blueprint.route('/<int:pk>', methods=['GET'])
def show(pk):
    post = Post.with_('user', 'attachment', 'comments.user').find_or_fail(pk)
    return render_template('posts/show.html', post=post)


@blueprint.route('/<int:pk>/update', methods=['GET', 'POST'])
def update(pk):

    post = Post.with_('attachment').where('user_id', session['auth']['id']).find_or_fail(pk)
    form = PostForm(obj=post)

    if request.method == 'POST' and form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        post.save()

        return redirect(url_for('posts.show', pk=post.id))

    return render_template('posts/form.html', form=form)


@blueprint.route('/<int:id>/delete', methods=['POST', 'DELETE'])
def delete(id):
    Post.where('user_id', session['auth']['id']).destroy(id)
    return redirect(url_for('posts.index'))


@blueprint.route('/<int:id>/comment', methods=['DELETE'])
def comment_create(id):

    post = Post.find_or_fail(id)

    comment = Comment()
    comment.commentable_id = id
    comment.commentable_type = 'posts'
    comment.user_id = session['auth']['id']
    comment.save()

    post.comments_count = post.comments_count + 1
    post.save()