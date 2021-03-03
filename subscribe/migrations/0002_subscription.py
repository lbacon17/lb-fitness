# Generated by Django 3.1.7 on 2021-03-03 21:25

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_id', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=60)),
                ('email_address', models.CharField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address_line1', models.CharField(max_length=80)),
                ('address_line2', models.CharField(blank=True, max_length=80, null=True)),
                ('town_or_city', models.CharField(max_length=50)),
                ('county_or_region', models.CharField(blank=True, max_length=50, null=True)),
                ('postcode', models.CharField(max_length=10)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('amount_due', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Subscriptions',
            },
        ),
    ]
