# Generated by Django 3.0.8 on 2020-09-04 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20200730_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=30, verbose_name='Brand name')),
                ('description', models.TextField(max_length=500, verbose_name='Brand description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=30, verbose_name='Category name')),
                ('description', models.TextField(max_length=500, verbose_name='Category description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=30, verbose_name='Product name')),
                ('description', models.TextField(max_length=750, verbose_name='Product description')),
                ('price', models.FloatField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('quantity', models.IntegerField(default=0)),
                ('is_avialable', models.BooleanField(default=True)),
                ('colors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.Color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]