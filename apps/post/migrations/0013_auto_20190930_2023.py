# Generated by Django 2.1.1 on 2019-09-30 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20190729_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
