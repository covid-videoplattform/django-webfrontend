# Generated by Django 3.0.4 on 2020-03-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200324_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmember',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
