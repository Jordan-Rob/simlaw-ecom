# Generated by Django 3.1.4 on 2020-12-09 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_auto_20201209_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('building_apartment_name', models.CharField(blank=True, max_length=200, null=True)),
                ('order_notes', models.CharField(blank=True, max_length=200, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='billing_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.billingdetails'),
        ),
    ]
