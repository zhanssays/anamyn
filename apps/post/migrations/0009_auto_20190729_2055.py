# Generated by Django 2.1.1 on 2019-07-29 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
