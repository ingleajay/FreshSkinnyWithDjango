# Generated by Django 3.2.4 on 2021-06-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_variation_variation_category'),
        ('cart', '0004_auto_20210629_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]