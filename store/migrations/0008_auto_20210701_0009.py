# Generated by Django 3.1.7 on 2021-06-30 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210630_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('size', 'size'), ('color', 'color')], max_length=100),
        ),
    ]