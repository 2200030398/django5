# Generated by Django 4.1.13 on 2024-03-15 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyfarm', '0004_rename_login_users_alter_users_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True),
        ),
    ]
