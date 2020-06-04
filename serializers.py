from marshmallow import Schema, fields, pre_load, post_dump

class LoginSchema(Schema):
    email = fields.Email()
    password = fields.Str(load_only=True)


class UserSchema(Schema):
    email = fields.Email()
    name = fields.Str()
    last_login_at = fields.DateTime()

    class Meta:
        fields = ("email", "name", "last_login_at")
        ordered = True


class CommentSchema(Schema):
    id = fields.Int()
    commentable_id = fields.Int()
    commentable_type = fields.Str()
    user = fields.Nested(UserSchema)
    body = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    class Meta:
        fields = ("id", "commentable_id", "commentable_type", "user", "body", "created_at", "updated_at")
        ordered = True


class CommentsSchema(CommentSchema):
    @post_dump
    def dump_comment(self, data, **kwargs):
        # data['comments'] = data['comments']
        return data


class PostIndexSchema(Schema):
    page = fields.Int()
    per_page = fields.Int()


class PostSchema(Schema):
    id = fields.Int()
    user = fields.Nested(UserSchema)
    title = fields.Str()
    body = fields.Str()
    comments_count = fields.Int()
    comments = fields.List(fields.Nested("CommentsSchema"))

    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    class Meta:
        fields = ("id", "user", "title", "body", "comments_count", "comments", "created_at", "updated_at")
        # fields = ("id", "user", "title", "body", "comments_count", "created_at", "updated_at")
        ordered = True


class PostsSchema(PostSchema):

    @post_dump
    def dump_article(self, data, **kwargs):
        data['user'] = data['user']
        return data

    # @post_dump(pass_many=True)
    # def dump_articles(self, data, many, **kwargs):
    #     return {
    #         'posts_count': len(data),
    #         'posts': data
    #     }


