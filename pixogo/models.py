from django.db import models

class Contact(models.Model):
        contact_id = models.AutoField(primary_key=True)
        contact_message = models.TextField(max_length=3000)

        def __str__(self):
                return 'Message no: ' + ' ' + str(self.contact_id)