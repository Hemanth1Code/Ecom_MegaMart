# Generated by Django 5.0.2 on 2024-03-26 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectStore', '0004_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='kidsCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(default=0, upload_to='projectStore/static/images')),
                ('price', models.FloatField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=150, null=True)),
                ('digitalItems', models.BooleanField(null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projectStore.category')),
            ],
        ),
        migrations.CreateModel(
            name='menCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(default=0, upload_to='projectStore/static/images')),
                ('price', models.FloatField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=150, null=True)),
                ('digitalItems', models.BooleanField(null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projectStore.category')),
            ],
        ),
        migrations.CreateModel(
            name='motorSportCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(default=0, upload_to='projectStore/static/images')),
                ('price', models.FloatField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=150, null=True)),
                ('digitalItems', models.BooleanField(null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projectStore.category')),
            ],
        ),
        migrations.CreateModel(
            name='newCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(default=0, upload_to='projectStore/static/images')),
                ('price', models.FloatField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=150, null=True)),
                ('digitalItems', models.BooleanField(null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projectStore.category')),
            ],
        ),
        migrations.CreateModel(
            name='sportCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(default=0, upload_to='projectStore/static/images')),
                ('price', models.FloatField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=150, null=True)),
                ('digitalItems', models.BooleanField(null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projectStore.category')),
            ],
        ),
        migrations.CreateModel(
            name='womenCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(default=0, upload_to='projectStore/static/images')),
                ('price', models.FloatField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=150, null=True)),
                ('digitalItems', models.BooleanField(null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projectStore.category')),
            ],
        ),
    ]
