# Generated by Django 2.2.9 on 2020-03-22 17:13

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_report_first_symptomatic'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
