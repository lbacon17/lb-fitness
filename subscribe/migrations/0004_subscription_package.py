# Generated by Django 3.1.7 on 2021-03-04 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0003_auto_20210303_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subscribe.package'),
        ),
    ]
