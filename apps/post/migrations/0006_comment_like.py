# Generated by Django 2.1.1 on 2019-07-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
