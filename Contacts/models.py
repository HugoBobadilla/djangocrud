from django.db import models

# Create your models here.
class Contact(models.Model):
  contactId = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=120)
  last_name = models.CharField(max_length=120)
  phone_number = models.CharField(max_length=30)
  address = models.CharField(max_length=150)

  class Meta:
    db_table = 'Contact'