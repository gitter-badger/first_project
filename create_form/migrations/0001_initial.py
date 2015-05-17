# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('max_participants', models.PositiveIntegerField()),
                ('current_participants', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('location', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event_category',
            fields=[
                ('event_category_id', models.AutoField(serialize=False, primary_key=True)),
                ('event_category_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Event_file_type',
            fields=[
                ('event_file_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('file_type', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Event_files',
            fields=[
                ('event_files_id', models.AutoField(serialize=False, primary_key=True)),
                ('event_file_type_id', models.ForeignKey(to='create_form.Event_file_type')),
                ('event_id', models.ForeignKey(to='create_form.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Event_gift',
            fields=[
                ('event_gift_id', models.AutoField(serialize=False, primary_key=True)),
                ('event_gift_name', models.CharField(max_length=40)),
                ('event_gift_description', models.CharField(max_length=200)),
                ('event_gift_amount', models.PositiveIntegerField()),
                ('event_id', models.ForeignKey(to='create_form.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Event_own_field',
            fields=[
                ('event_own_field_id', models.AutoField(serialize=False, primary_key=True)),
                ('own_field_title', models.CharField(max_length=40)),
                ('own_field_description', models.TextField()),
                ('own_field_type', models.CharField(max_length=40)),
                ('event_id', models.ForeignKey(to='create_form.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Event_schedule',
            fields=[
                ('event_schedule_id', models.AutoField(serialize=False, primary_key=True)),
                ('event_schedule_name', models.CharField(max_length=40)),
                ('event_start_date', models.DateTimeField()),
                ('event_end_date', models.DateTimeField()),
                ('event_description', models.TextField()),
                ('event_id', models.ForeignKey(to='create_form.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Event_status',
            fields=[
                ('event_status_id', models.AutoField(serialize=False, primary_key=True)),
                ('event_status_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_category_id',
            field=models.ForeignKey(to='create_form.Event_category'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_status_id',
            field=models.ForeignKey(to='create_form.Event_status'),
        ),
        migrations.AddField(
            model_name='event',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
