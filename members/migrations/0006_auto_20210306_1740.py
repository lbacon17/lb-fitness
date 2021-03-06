# Generated by Django 3.1.7 on 2021-03-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20210306_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='default_address_line1',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='default_address_line2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='default_county_or_region',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='default_email_address',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='default_postcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='default_town_or_city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
