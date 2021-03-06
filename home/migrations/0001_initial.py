# Generated by Django 2.0.7 on 2018-07-10 01:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='slides/')),
                ('b_image', models.ImageField(upload_to='slides/')),
                ('Link', models.TextField(max_length=200, null=True)),
                ('Description', models.TextField(max_length=200, null=True)),
                ('Created_At', models.DateTimeField(auto_now_add=True)),
                ('Modified_At', models.DateTimeField(auto_now_add=True)),
                ('Status', models.NullBooleanField(default=True)),
                ('Created_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name_cre', to=settings.AUTH_USER_MODEL)),
                ('Modified_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name_update', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
