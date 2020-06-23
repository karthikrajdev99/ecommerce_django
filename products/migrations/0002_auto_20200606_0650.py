# Generated by Django 3.0.4 on 2020-06-06 01:20

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='picture'),
        ),
    ]
