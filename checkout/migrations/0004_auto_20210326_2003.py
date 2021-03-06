# Generated by Django 3.1.7 on 2021-03-26 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210326_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='shoporder',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
    ]
