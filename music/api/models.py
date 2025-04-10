from django.db import models

class Label(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()

    city = models.CharField(max_length = 255)
    adress = models.TextField()

class Artist(models.Model):
    stage_name = models.CharField(max_length = 255)
    bio = models.TextField()

    income = models.FloatField()

    label =  models.ForeignKey(Label, on_delete = models.CASCADE,related_name = 'artists')
