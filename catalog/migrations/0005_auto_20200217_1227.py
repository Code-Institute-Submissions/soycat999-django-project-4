# Generated by Django 2.2.4 on 2020-02-17 12:27

import datetime
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_course_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('publisher', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('image', pyuploadcare.dj.models.ImageField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
            ],
            options={
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
    ]