from datetime import datetime
from flask import Blueprint, session, request, redirect, render_template, url_for
from forms import PostForm

from models import Post

blueprint = Blueprint('posts', __name__)


@blueprint.route('/', methods=['GET'])
def index():

    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 15)

    posts = Post.with_('user').order_by('id', 'desc').paginate(per_page, page)

    # print(posts.serialize())

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

        return redirect(url_for('posts.index'))

    return render_template('posts/form.html', form=form)


@blueprint.route('/<int:pk>', methods=['GET'])
def show(pk):
    post = Post.with_('user').find_or_fail(pk)
    return render_template('posts/show.html', post=post)


@blueprint.route('/<int:pk>/update', methods=['GET', 'POST'])
def update(pk):

    post = Post.find_or_fail(pk)
    form = PostForm(obj=post)

    if request.method == 'POST' and form.validate_on_submit():

        post.title = form.title.data
        post.body = form.body.data
        post.save()

        return redirect(url_for('posts.show', pk=post.id))

    return render_template('posts/form.html', form=form)

@blueprint.route('/<int:pk>/delete', methods=['POST', 'DELETE'])
def delete(pk):
    Post.destroy(pk)
    return redirect(url_for('posts.index'))