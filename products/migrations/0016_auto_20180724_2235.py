# Generated by Django 2.0.7 on 2018-07-24 15:35

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20180724_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_new',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='color',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Orange', 'Orange'), ('Blue', 'Blue'), ('Black', 'Black'), ('White', 'White'), ('Grey', 'Grey'), ('Red', 'Red'), ('Green', 'Green')], default='Black', max_length=50),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('S', 'S'), ('XL', 'XL'), ('L', 'L'), ('XXL', 'XXL'), ('M', 'M')], default='L', max_length=50),
        ),
    ]
