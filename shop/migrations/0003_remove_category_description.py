# Generated by Django 2.0.3 on 2018-04-29 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
