# Generated by Django 2.1.1 on 2019-12-08 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20191208_2227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planningchild',
            old_name='date_of_child',
            new_name='date_birth_baby',
        ),
    ]
