# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    SEX_CHOICE= [('M','Male'),('F','Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField( max_length=10)
    breed = models.CharField( max_length=50, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICE, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField("Vaccine",blank=True)

class Vaccine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    