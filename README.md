# flask_orator
flask, flask_orator

### database configs
```python
app.config['ORATOR_DATABASES'] = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'flask_orator',
        'user': 'sjahn',
        'password': '1234',
        'prefix': '',
        'log_queries': True
    }
}
```

### database migration
* create migration: `python db.py make:migration create_users_table --table users --create`
* run migration: `python db.py migrate`