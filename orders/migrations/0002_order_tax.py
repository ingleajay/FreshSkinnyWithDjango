# Generated by Django 3.2.4 on 2021-07-02 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
