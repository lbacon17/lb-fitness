# Generated by Django 3.1.7 on 2021-03-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0006_auto_20210307_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]