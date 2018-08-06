# Generated by Django 2.0.7 on 2018-07-22 15:51

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20180721_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='color',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Green', 'Xanh nước biển'), ('Orange', 'Da cam'), ('Black', 'Đen'), ('Blue', 'Xanh da trời'), ('Grey', 'Xám'), ('Red', 'Đỏ'), ('White', 'Trắng')], default='Black', max_length=50),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('XL', 'XL'), ('XXL', 'XXL'), ('L', 'L'), ('S', 'S'), ('M', 'M')], default='L', max_length=50),
        ),
        migrations.AlterField(
            model_name='product_image',
            name='image1',
            field=models.ImageField(default='products/image-none.png', upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product_image',
            name='image2',
            field=models.ImageField(default='products/image-none.png', upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product_image',
            name='image3',
            field=models.ImageField(default='products/image-none.png', upload_to='products/'),
        ),
    ]
