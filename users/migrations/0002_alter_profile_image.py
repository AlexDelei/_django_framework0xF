# Generated by Django 5.0.1 on 2024-02-08 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='range.jpeg', upload_to='profile_pics'),
        ),
    ]
