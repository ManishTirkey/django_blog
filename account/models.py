from django.db import models

# Create your models here.

class Contact(models.Model):
    con_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    ph_no = models.CharField(max_length=50, default="")
    comments = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.full_name
