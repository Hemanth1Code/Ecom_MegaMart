# Generated by Django 5.0.2 on 2024-03-29 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectStore', '0011_rename_quantityofitems_ordereditem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=0, upload_to='projectStore/static/imagesshoes'),
        ),
    ]