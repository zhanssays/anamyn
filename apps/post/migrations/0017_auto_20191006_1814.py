# Generated by Django 2.1.1 on 2019-10-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(),
        ),
    ]
