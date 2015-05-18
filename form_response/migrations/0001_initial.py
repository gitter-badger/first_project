# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('create_form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormFieldInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('form_field', models.ForeignKey(to='create_form.OwnField')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_assessment', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('event_fraudulent', models.BooleanField(default=False)),
                ('registration_confirmed', models.BooleanField(default=False)),
                ('event', models.ForeignKey(to='create_form.Event')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationInstanceGifts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('gift', models.ForeignKey(to='create_form.Gift')),
                ('registration_instance', models.ForeignKey(to='form_response.RegistrationInstance')),
            ],
        ),
        migrations.AddField(
            model_name='registrationinstance',
            name='gifts',
            field=models.ManyToManyField(to='create_form.Gift', through='form_response.RegistrationInstanceGifts'),
        ),
        migrations.AddField(
            model_name='formfieldinstance',
            name='registration_instance',
            field=models.ManyToManyField(to='form_response.RegistrationInstance'),
        ),
    ]
