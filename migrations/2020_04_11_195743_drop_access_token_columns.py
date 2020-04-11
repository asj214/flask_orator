from orator.migrations import Migration


class DropAccessTokenColumns(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('users') as table:
            table.drop_index('users_access_token_index')
            table.drop_column('access_token')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('users') as table:
            pass
