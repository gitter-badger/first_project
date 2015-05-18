from django.contrib.auth.models import User
from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=40)

class Category(models.Model):
    name = models.CharField(max_length=40)

class Event(models.Model):
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=200)
    max_participants = models.PositiveIntegerField()
    price = models.FloatField()
    location = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()

class FileType(models.Model):
    file_type = models.CharField(max_length=40)

class Files(models.Model):
    file_name = models.CharField(max_length=40)
    file_type = models.ForeignKey(FileType)
    event = models.ForeignKey(Event)

class Schedule(models.Model):
    name = models.CharField(max_length=40)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    event = models.ForeignKey(Event)

class Gift(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    event = models.ForeignKey(Event)

class OwnField(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    field_type = models.CharField(max_length=40)
    event = models.ForeignKey(Event)
