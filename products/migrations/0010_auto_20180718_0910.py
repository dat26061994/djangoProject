# Generated by Django 2.0.7 on 2018-07-18 02:10

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20180718_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='color',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Red', 'Đỏ'), ('Orange', 'Da cam'), ('White', 'Trắng'), ('Green', 'Xanh nước biển'), ('Blue', 'Xanh da trời'), ('Grey', 'Xám'), ('Black', 'Đen')], default='Black', max_length=50),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('L', 'L'), ('S', 'S'), ('M', 'M'), ('XXL', 'XXL'), ('XL', 'XL')], default='L', max_length=50),
        ),
    ]
