# Generated by Django 3.1.4 on 2021-01-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('short_url', models.CharField(max_length=200)),
                ('visits', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
