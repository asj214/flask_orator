from orator.migrations import Migration


class AfterTest(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('posts') as table:
            table.integer('comments_count').default(0).nullable().after('body')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('posts') as table:
            pass
