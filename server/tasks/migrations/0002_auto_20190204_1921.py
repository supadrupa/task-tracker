# Generated by Django 2.1.5 on 2019-02-04 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='description',
            old_name='description',
            new_name='text',
        ),
    ]
