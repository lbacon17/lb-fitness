# Generated by Django 3.1.7 on 2021-03-06 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_member_default_phone_number'),
        ('subscribe', '0004_subscription_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptions', to='members.member'),
        ),
    ]