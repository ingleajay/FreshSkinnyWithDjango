# Generated by Django 3.2.4 on 2021-07-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210702_2316'),
        ('cart', '0010_alter_cartitem_variations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]
