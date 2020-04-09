from datetime import datetime
from flask import Blueprint, request, redirect, url_for, jsonify
from marshmallow import Schema, fields, pprint

import wtforms_json
from forms import UserForm, LoginForm

from werkzeug.security import generate_password_hash, check_password_hash

from models import User

class UserSchema(Schema):
    email = fields.Email()
    name = fields.Str()
    last_login_at = fields.Date()


wtforms_json.init()
api_auth_v1 = Blueprint('api_auth_v1', __name__)

@api_auth_v1.route('/login', methods=['POST'])
def login():
    form = LoginForm.from_json(request.json)
    print(form.validate())
    print(form.data)
    print(request.json)

    if form.validate():
        return jsonify({'status': 200})
    else:
        return jsonify({'status': 400})

    return ''