# Generated by Django 4.1.13 on 2024-03-15 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyfarm', '0006_buy'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='type',
            field=models.CharField(default='', max_length=50),
        ),
    ]