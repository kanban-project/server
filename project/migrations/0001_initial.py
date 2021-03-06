# Generated by Django 3.0.6 on 2020-05-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
