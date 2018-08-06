# Generated by Django 2.0.7 on 2018-07-25 13:28

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20180724_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='color',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Black', 'Black'), ('White', 'White'), ('Blue', 'Blue'), ('Red', 'Red'), ('Grey', 'Grey'), ('Green', 'Green'), ('Orange', 'Orange')], default='Black', max_length=50),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('XL', 'XL'), ('XXL', 'XXL'), ('L', 'L'), ('S', 'S'), ('M', 'M')], default='L', max_length=50),
        ),
    ]
