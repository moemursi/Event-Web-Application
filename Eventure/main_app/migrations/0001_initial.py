# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-30 02:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendeeName', models.CharField(default='', max_length=256)),
                ('attendeeID', models.CharField(default='', max_length=8)),
                ('userAttendeeID', models.IntegerField(null=True)),
                ('email', models.EmailField(default='', max_length=256)),
                ('RSVPStatus', models.IntegerField(blank=True, choices=[(1, 'Not Attending'), (2, 'Maybe'), (3, 'Attending')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EventInfo',
            fields=[
                ('id', models.CharField(default='', max_length=12, primary_key=True, serialize=False)),
                ('type', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('description', models.TextField()),
                ('eventPhoto', models.ImageField(blank=True, default=None, upload_to='event_photos', verbose_name='picture')),
                ('eventCategory', models.IntegerField(blank=True, choices=[(0, 'Misc'), (1, 'Party'), (2, 'Education'), (3, 'Music'), (4, 'Food and Drink'), (5, 'Movies'), (6, 'Arts'), (7, 'Technology'), (8, 'Health'), (9, 'Out Doors'), (10, 'Sports')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('amount', models.IntegerField(default=0)),
                ('amountTaken', models.PositiveIntegerField(default=0)),
                ('isTaken', models.BooleanField(default=False)),
                ('eventID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.EventInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('pollID', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=200)),
                ('eventID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.EventInfo')),
            ],
        ),
        migrations.CreateModel(
            name='TakenItem',
            fields=[
                ('itemBeingBroughtID', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('comment', models.TextField(default='')),
                ('attendeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Attendee')),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.EventInfo')),
                ('itemLinkID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Item')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('profilePhoto', models.ImageField(blank=True, default=None, upload_to='profile_photos')),
                ('city', models.CharField(max_length=64, verbose_name='city')),
                ('state', localflavor.us.models.USStateField(default='TX', max_length=2, verbose_name='state')),
                ('zip', models.CharField(max_length=5, verbose_name='zip code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Attendee')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Poll')),
            ],
        ),
        migrations.AddField(
            model_name='eventinfo',
            name='userProfile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.UserProfile'),
        ),
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Poll'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='eventID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.EventInfo'),
        ),
    ]
