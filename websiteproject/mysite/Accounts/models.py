from django.db import models

# Create your models here.
class Therapist(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
class Meta:
    ordering = ['firstname', 'lastname']

    def __str__(self):
        return self.firstname + " " + str(self.lastname)