# Generated by Django 2.2.4 on 2020-02-28 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_remove_games_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='cost',
            field=models.FloatField(null=True),
        ),
    ]
