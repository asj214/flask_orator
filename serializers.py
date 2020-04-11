from marshmallow import Schema, fields, pre_load, post_dump

class LoginSchema(Schema):
    email = fields.Email()
    password = fields.Str(load_only=True)

class UserSchema(Schema):
    email = fields.Email()
    name = fields.Str()
    last_login_at = fields.Date()

    class Meta:
        fields = ("email", "name", "last_login_at")
        ordered = True