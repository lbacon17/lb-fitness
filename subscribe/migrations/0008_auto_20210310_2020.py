# Generated by Django 3.1.7 on 2021-03-10 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0007_subscription_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='monthly_rate',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='amount_due',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
        ),
        migrations.CreateModel(
            name='SubscriptionCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('monthly_rate', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscribe.package')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_count', to='subscribe.subscription')),
            ],
        ),
    ]