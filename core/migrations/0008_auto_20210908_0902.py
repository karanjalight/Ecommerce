# Generated by Django 3.2.6 on 2021-09-08 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkoutaddress',
            name='location',
        ),
        migrations.RemoveField(
            model_name='checkoutaddress',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='checkoutaddress',
            name='purchase_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='checkoutaddress',
            name='street_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='checkoutaddress',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
