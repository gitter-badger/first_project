from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Event_status(models.Model):
    def __init__(self, event_status_id, event_status_name):
        self.event_status_id = event_status_id
        self.event_status_name = event_status_name
    
    event_status_id = models.AutoField(primary_key=True)
    event_status_name = models.CharField(max_length=40)


class Event_category(models.Model):
    def __init__(self, event_category_id, event_category_name):
        self.event_category_id = event_category_id
        self.event_category_name = event_category_name
    
    event_category_id = models.AutoField(primary_key=True)
    event_category_name = models.CharField(max_length=40)


class Event(models.Model):
    def __init__(self, event_id, user_id, event_status_id, event_category_id, title, category, status, max_participants, current_participants, price, location, start_date, end_date, description):
        self.event_id = event_id
        self.user_id = user_id
        self.event_status_id = event_status_id
        self.event_category_id = event_category_id
        self.title = title
        self.max_participants = max_participants
        self.current_participants = current_participants
        self.price = price
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
    
    event_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    event_status_id = models.ForeignKey(Event_status)
    event_category_id = models.ForeignKey(Event_category)
    title = models.CharField(max_length=200)
    max_participants = models.PositiveIntegerField()
    current_participants = models.PositiveIntegerField()
    price = models.FloatField()
    location = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()


class Event_file_type(models.Model):
    def __init__(self, event_file_type_id, file_type):
        self.event_file_type_id = event_file_type_id
        self.file_type = file_type
    
    event_file_type_id = models.AutoField(primary_key=True)
    file_type = models.CharField(max_length=40)


class Event_files(models.Model):
    def __init__(self, event_files_id, event_file_type_id, event_id):
        self.event_files_id = event_files_id
        self.event_file_type_id = event_file_type_id
        self.event_id = event_id
    
    event_files_id = models.AutoField(primary_key=True)
    event_file_type_id = models.ForeignKey(Event_file_type)
    event_id = models.ForeignKey(Event)


class Event_schedule(models.Model):
    def __init__(self, event_schedule_id, event_schedule_name, event_start_date, event_end_date, event_description, event_id):
        self.event_schedule_id = event_schedule_id
        self.event_schedule_name = event_schedule_name
        self.event_start_date = event_start_date
        self.event_end_date = event_end_date
        self.event_description = event_description
        self.event_id = event_id
    
    event_schedule_id = models.AutoField(primary_key=True)
    event_schedule_name = models.CharField(max_length=40)
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    event_description = models.TextField()
    event_id = models.ForeignKey(Event)


class Event_gift(models.Model):
    def __init__(self, event_gift_id, event_id, event_gift_name, event_gift_description, event_gift_amount):
        self.event_gift_id = event_gift_id
        self.event_id = event_id
        self.event_gift_name = event_gift_name
        self.event_gift_description = event_gift_description
        self.event_gift_amount = event_gift_amount
    
    event_gift_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event)
    event_gift_name = models.CharField(max_length=40)
    event_gift_description = models.CharField(max_length=200)
    event_gift_amount = models.PositiveIntegerField()


class Event_own_field(models.Model):
    def __init__(self, event_own_field_id, own_field_title, own_field_description, own_field_type, event_id):
    	self.event_own_field_id = event_own_field_id
        self.own_field_title = own_field_title
        self.own_field_description = own_field_description
        self.own_field_type = own_field_type
        self.event_id = event_id
    
    event_own_field_id = models.AutoField(primary_key=True)
    own_field_title = models.CharField(max_length=40)
    own_field_description = models.TextField()
    own_field_type = models.CharField(max_length=40)
    event_id = models.ForeignKey(Event)