# Generated by Django 3.1.2 on 2020-10-13 13:23

from django.db import migrations, models
import django.db.models.deletion
import main_app.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(default=None, max_length=150)),
                ('city', models.CharField(default=None, max_length=150)),
                ('state', models.CharField(default=None, max_length=150)),
                ('country', models.CharField(default=None, max_length=150)),
                ('zip_code', models.CharField(max_length=150)),
                ('hash', models.UUIDField(default=None, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.IntegerField(default=main_app.utils.id_generator, unique=True)),
                ('description', models.CharField(blank=True, max_length=5000)),
                ('name', models.CharField(max_length=150)),
                ('image', models.FileField(upload_to=main_app.utils.upload_directory_path)),
                ('is_valid', models.BooleanField(default=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.address')),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.IntegerField(default=main_app.utils.id_generator, unique=True)),
                ('description', models.CharField(blank=True, max_length=5000)),
                ('image', models.FileField(upload_to=main_app.utils.upload_directory_path)),
                ('number', models.IntegerField()),
                ('index', models.IntegerField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.building')),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=150)),
                ('is_reserved', models.BooleanField(default=False)),
                ('image', models.FileField(upload_to=main_app.utils.upload_directory_path)),
                ('index', models.IntegerField()),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.floor')),
            ],
        ),
    ]
