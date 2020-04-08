from orator.migrations import Migration

# python db.py make:migration create_users_table --table=users --create

class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('email', 75)
            table.string('password')
            table.string('name', 75)

            table.timestamp('last_login_at').nullable()
            table.timestamps()
            table.soft_deletes()

            table.unique(['email', 'deleted_at'])

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
