# Generated by Django 2.0.7 on 2018-07-17 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180716_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(max_length=100)),
                ('dimensions', models.CharField(max_length=100)),
                ('materials', models.IntegerField(max_length=100)),
                ('color', models.CharField(choices=[('Grey', 'Xám'), ('Black', 'Đen'), ('Orange', 'Da cam'), ('Green', 'Xanh nước biển'), ('Red', 'Đỏ'), ('Blue', 'Xanh da trời'), ('White', 'Trắng')], default='Black', max_length=10)),
                ('size', models.CharField(choices=[('S', 'S'), ('XL', 'XL'), ('XXL', 'XXL'), ('L', 'L'), ('M', 'M')], default='L', max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_detail', to='products.Product')),
            ],
        ),
        migrations.AlterField(
            model_name='product_image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='products.Product'),
        ),
    ]
