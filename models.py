from app import db
from orator import Model, SoftDeletes
from orator.orm import belongs_to, has_many


Model.set_connection_resolver(db)

class User(SoftDeletes, Model):
    __table__ = 'users'
    __fillable__ = ['email', 'name', 'last_login_at']
    __dates__ = ['deleted_at']

    @has_many
    def posts(self):
        return Post

class Post(SoftDeletes, Model):
    __table__ = 'posts'
    __fillable__ = ['user_id', 'title', 'body']
    __dates__ = ['deleted_at']

    @belongs_to('user_id', 'id')
    def user(self):
        return User