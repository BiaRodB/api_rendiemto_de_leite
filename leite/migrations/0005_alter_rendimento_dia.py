# Generated by Django 4.2.2 on 2023-07-10 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leite', '0004_alter_rendimento_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendimento',
            name='dia',
            field=models.CharField(max_length=10),
        ),
    ]