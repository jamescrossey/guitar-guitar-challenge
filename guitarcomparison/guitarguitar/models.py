from django.db import models

# Create your models here.
class Genres(models.Model):
    genre = models.CharField()

class Names(models.Model):
    Names = models.CharField()

class genresNames(models.Model):
    genre = models.ForeignKey(Genres)
    names = models.ForeignKey(Names)


