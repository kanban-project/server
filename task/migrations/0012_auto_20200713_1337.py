# Generated by Django 3.0.6 on 2020-07-13 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_auto_20200713_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.SmallIntegerField(choices=[(1, 'high'), (2, 'middle'), (3, 'low')], default=2),
        ),
    ]