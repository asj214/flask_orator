from orator.migrations import Migration


class CreateCommentsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('comments') as table:
            table.increments('id')
            table.integer('commentable_id')
            table.string('commentable_type')
            table.integer('user_id')
            table.text('body')
            table.timestamps()
            table.soft_deletes()
            table.index(['commentable_id', 'commentable_type', 'deleted_at'], name='comments')


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('comments')