from datetime import datetime
from flask import Blueprint, session, request, redirect, render_template, url_for
from forms import PostForm

from models import Post

post_controller = Blueprint('post_controller', __name__)

@post_controller.route('/', methods=['GET'])
def index():

    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 15)

    posts = Post.with_('user').order_by('id', 'desc').paginate(per_page, page)

    # print(posts.serialize())

    return render_template('posts/list.html', posts=posts)

@post_controller.route('/create', methods=['GET', 'POST'])
def create():

    if not 'auth' in session:
        return redirect(url_for('user_controller.login', redirect_url=request.url))

    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():

        post = Post()
        post.user_id = session['auth']['id']
        post.title = form.title.data
        post.body = form.body.data
        post.save()

        return redirect(url_for('post_controller.index'))

    return render_template('posts/form.html', form=form)


@post_controller.route('/<int:pk>', methods=['GET'])
def show(pk):
    post = Post.with_('user').find_or_fail(pk)
    return render_template('posts/show.html', post=post)


@post_controller.route('/<int:pk>/update', methods=['GET', 'POST'])
def update(pk):

    post = Post.find_or_fail(pk)
    form = PostForm(obj=post)

    if request.method == 'POST' and form.validate_on_submit():

        post.title = form.title.data
        post.body = form.body.data
        post.save()

        return redirect(url_for('post_controller.show', pk=post.id))

    return render_template('posts/form.html', form=form)

@post_controller.route('/<int:pk>/delete', methods=['POST', 'DELETE'])
def delete(pk):
    Post.destroy(pk)
    return redirect(url_for('post_controller.index'))