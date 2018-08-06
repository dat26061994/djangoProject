# Generated by Django 2.0.7 on 2018-08-03 03:23

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20180731_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupouns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('discouns', models.FloatField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.NullBooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cate_pr', to='products.Product')),
            ],
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='color',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Red', 'Red'), ('Grey', 'Grey'), ('Green', 'Green'), ('White', 'White'), ('Black', 'Black'), ('Orange', 'Orange'), ('Blue', 'Blue')], default='Black', max_length=50),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('S', 'S'), ('L', 'L'), ('XL', 'XL'), ('M', 'M'), ('XXL', 'XXL')], default='L', max_length=50),
        ),
    ]
