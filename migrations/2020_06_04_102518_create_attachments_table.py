from orator.migrations import Migration


class CreateAttachmentsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('attachments') as table:
            table.increments('id')
            table.integer('attachment_id')
            table.string('attachment_type')
            table.integer('user_id')
            table.string('url')
            table.timestamps()
            table.soft_deletes()
            table.index(['attachment_id', 'attachment_type', 'deleted_at'], name='attachment')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('attachments')
