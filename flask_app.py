import json
from flask import Flask, render_template
from flask_orator import Orator
from flask_jwt_extended import JWTManager

import logging

cfg: dict = {}
with open('cfg.json', encoding='utf-8') as cfg_json:
    cfg = json.loads(cfg_json.read())

app = Flask(__name__)
app.secret_key = 'secret'
app.config['JSON_SORT_KEYS'] = False
app.config['ORATOR_DATABASES'] = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': cfg['database']['host'],
        'database': cfg['database']['database'],
        'user': cfg['database']['user'],
        'password': cfg['database']['password'],
        'prefix': '',
        'log_queries': cfg['database']['log_queries']
    }
}

app.config['JWT_SECRET_KEY'] = 'qwe123'  # Change this!
app.config['JWT_TOKEN_LOCATION'] = ['headers'] # headers', 'cookies', 'query_string', 'json'

db = Orator(app)
jwt = JWTManager(app)


logger = logging.getLogger('orator.connection.queries')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(elapsed_time)sms %(query)s'
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger.addHandler(handler)


from web import users, posts
from api import (
    api_auth,
    api_posts
)

# register blueprint
app.register_blueprint(users.blueprint, url_prefix='/users')
app.register_blueprint(posts.blueprint, url_prefix='/posts')
app.register_blueprint(api_auth.blueprint, url_prefix='/api/auth')
app.register_blueprint(api_posts.blueprint, url_prefix='/api/posts')


@app.cli.command()
def routes():
    'Display registered routes'
    rules = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        rules.append((rule.endpoint, methods, str(rule)))

    sort_by_rule = operator.itemgetter(2)
    for endpoint, methods, rule in sorted(rules, key=sort_by_rule):
        route = '{:50s} {:25s} {}'.format(endpoint, methods, rule)
        print(route)

@app.route('/')
def index():
    return render_template('main/index.html')
