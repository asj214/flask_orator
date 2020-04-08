from orator.seeds import Seeder
from orator.orm import Factory

from app import db
from models import User, Post

# python db.py make:seed posts_table_seeder
# python db.py db:seed --seeder posts_table_seeder


factory = Factory()

@factory.define(Post)
def posts_factory(faker):
    return {
        'name': faker.name(),
        'email': faker.email(),
        'password': generate_password_hash('1234')
    }

class PostsTableSeeder(Seeder):

    factory = factory

    def run(self):
        """
        Run the database seeds.
        """
        self.factory(Post, 50).create()

