# Generated by Django 3.2.4 on 2021-07-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
    ]