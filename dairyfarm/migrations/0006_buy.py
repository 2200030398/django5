# Generated by Django 4.1.13 on 2024-03-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyfarm', '0005_remove_users_id_users_username_alter_users_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=10)),
                ('cname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Buy',
            },
        ),
    ]
