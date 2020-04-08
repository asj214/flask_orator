from orator.seeds import Seeder

from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models import User

# python db.py make:seed first_user_table_seeder
# python db.py db:seed --seeder first_user_table_seeder

class FirstUserTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('users').insert({
            'name': 'sjahn',
            'email': 'asj214@naver.com',
            'password': generate_password_hash('1234')
        })

