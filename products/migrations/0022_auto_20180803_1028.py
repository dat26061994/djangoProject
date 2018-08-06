# Generated by Django 2.0.7 on 2018-08-03 03:28

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20180803_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupouns',
            old_name='discouns',
            new_name='discount',
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='color',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Red', 'Red'), ('White', 'White'), ('Orange', 'Orange'), ('Green', 'Green'), ('Grey', 'Grey'), ('Blue', 'Blue'), ('Black', 'Black')], default='Black', max_length=50),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('S', 'S'), ('M', 'M'), ('XXL', 'XXL'), ('L', 'L'), ('XL', 'XL')], default='L', max_length=50),
        ),
    ]