# Generated by Django 3.1.7 on 2021-03-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210320_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoporder',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]