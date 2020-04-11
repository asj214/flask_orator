from orator.migrations import Migration


class AddAccessTokenColumns(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('users') as table:
            table.string('access_token').nullable().after('name').index()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('users') as table:
            table.drop_column('access_token')
            table.drop_index('users_access_token_index')