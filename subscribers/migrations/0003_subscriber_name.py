# Generated by Django 3.1.7 on 2021-03-03 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0002_auto_20210303_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]