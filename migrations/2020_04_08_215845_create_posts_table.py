from orator.migrations import Migration

# python db.py make:migration create_posts_table --table=posts --create

class CreatePostsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('posts') as table:
            table.increments('id')
            table.integer('user_id')
            table.string('title')
            table.text('body')
            table.timestamps()
            table.soft_deletes()
            table.index(['user_id', 'deleted_at'], name='user_posts')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('posts')
