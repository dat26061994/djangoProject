# Generated by Django 2.0.7 on 2018-07-17 17:05

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20180717_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='color',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Red', 'Đỏ'), ('Blue', 'Xanh da trời'), ('White', 'Trắng'), ('Green', 'Xanh nước biển'), ('Grey', 'Xám'), ('Orange', 'Da cam'), ('Black', 'Đen')], default='Black', max_length=50),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('XXL', 'XXL'), ('M', 'M'), ('XL', 'XL'), ('L', 'L'), ('S', 'S')], default='L', max_length=50),
        ),
    ]
