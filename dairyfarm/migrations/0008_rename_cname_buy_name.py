# Generated by Django 4.1.13 on 2024-03-15 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dairyfarm', '0007_buy_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buy',
            old_name='cname',
            new_name='name',
        ),
    ]
