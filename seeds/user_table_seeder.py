from orator.seeds import Seeder
from orator.orm import Factory

from faker import Faker

from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models import User


# python db.py make:seed user_table_seeder
# python db.py db:seed --seeder user_table_seeder

factory = Factory()

ko_faker = Faker('ko_KR')

@factory.define(User)
def users_factory(faker):

    return {
        'name': ko_faker.name(),
        'email': faker.email(),
        'password': generate_password_hash('1234')
    }

class UserTableSeeder(Seeder):

    factory = factory

    def run(self):
        """
        Run the database seeds.
        """
        

        self.factory(User, 50).create()
