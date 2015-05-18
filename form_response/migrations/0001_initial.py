# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('create_form', '0002_auto_20150518_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form_field_instance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('formField', models.ForeignKey(to='create_form.OwnField')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eventAssessment', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('eventFraudulent', models.BooleanField(default=False)),
                ('registrationConfirmed', models.BooleanField(default=False)),
                ('event', models.ForeignKey(to='create_form.Event')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationInstanceGifts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('gift', models.ForeignKey(to='create_form.Gift')),
                ('registrationInstance', models.ForeignKey(to='form_response.RegistrationInstance')),
            ],
        ),
        migrations.AddField(
            model_name='registrationinstance',
            name='gifts',
            field=models.ManyToManyField(to='create_form.Gift', through='form_response.RegistrationInstanceGifts'),
        ),
        migrations.AddField(
            model_name='form_field_instance',
            name='registrationInstance',
            field=models.ManyToManyField(to='form_response.RegistrationInstance'),
        ),
    ]
