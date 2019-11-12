# Generated by Django 2.1.1 on 2019-11-07 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=100)),
                ('marriage_status', models.CharField(max_length=100)),
                ('pregnant', models.BooleanField(default=False)),
                ('gestation', models.DateTimeField()),
                ('sex_of_child', models.CharField(max_length=100)),
            ],
        ),
    ]