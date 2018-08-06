# Generated by Django 2.0.7 on 2018-07-23 01:30

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20180722_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='color',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('White', 'Trắng'), ('Red', 'Đỏ'), ('Grey', 'Xám'), ('Orange', 'Da cam'), ('Green', 'Xanh nước biển'), ('Black', 'Đen'), ('Blue', 'Xanh da trời')], default='Black', max_length=50),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('M', 'M'), ('XXL', 'XXL'), ('XL', 'XL'), ('L', 'L'), ('S', 'S')], default='L', max_length=50),
        ),
    ]