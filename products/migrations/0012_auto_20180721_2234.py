# Generated by Django 2.0.7 on 2018-07-21 15:34

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20180721_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='color',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Grey', 'Xám'), ('Orange', 'Da cam'), ('Green', 'Xanh nước biển'), ('Red', 'Đỏ'), ('Blue', 'Xanh da trời'), ('Black', 'Đen'), ('White', 'Trắng')], default='Black', max_length=50),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='dimensions',
            field=models.CharField(default='1', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='materials',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('S', 'S'), ('XL', 'XL'), ('XXL', 'XXL'), ('M', 'M'), ('L', 'L')], default='L', max_length=50),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='weight',
            field=models.FloatField(default='1', max_length=100, null=True),
        ),
    ]
