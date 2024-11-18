from django.db import models

# Create your models here.
class Contact(models.Model):
    konu = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=500)
    message = models.TextField(blank = True)

    def __str__(self):
        return self.email