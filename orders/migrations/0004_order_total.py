# Generated by Django 2.0.7 on 2018-08-04 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180803_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0, max_length=200),
        ),
    ]
