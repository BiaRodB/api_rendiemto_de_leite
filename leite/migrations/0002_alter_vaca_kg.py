# Generated by Django 4.2.2 on 2023-07-04 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaca',
            name='kg',
            field=models.FloatField(max_length=8),
        ),
    ]
