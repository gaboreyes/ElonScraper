# Generated by Django 3.0.3 on 2020-03-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spacex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('fecha', models.CharField(max_length=25)),
            ],
        ),
    ]