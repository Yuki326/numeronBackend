# Generated by Django 3.1.14 on 2022-02-05 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220205_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guess',
            name='created_at',
        ),
    ]
