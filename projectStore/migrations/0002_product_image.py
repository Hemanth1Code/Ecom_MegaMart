# Generated by Django 5.0.2 on 2024-03-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectStore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=0, upload_to='static/images'),
            preserve_default=False,
        ),
    ]
