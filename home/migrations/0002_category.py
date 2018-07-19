# Generated by Django 2.0.7 on 2018-07-10 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='categories/')),
                ('status', models.NullBooleanField(default=True)),
                ('Created_At', models.DateTimeField(auto_now_add=True)),
                ('Modified_At', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]