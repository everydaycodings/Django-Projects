# Generated by Django 3.1 on 2020-09-05 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0004_auto_20200904_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpost',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Image'),
        ),
    ]
