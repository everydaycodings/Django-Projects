# Generated by Django 3.1 on 2020-09-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Breast_Cancer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='result',
            field=models.IntegerField(choices=[(0, 'Cancer'), (1, 'Non-Cancer')], default=1, verbose_name='Result'),
        ),
    ]
