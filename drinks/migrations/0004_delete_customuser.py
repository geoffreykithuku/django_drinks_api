# Generated by Django 5.0.2 on 2024-02-25 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0003_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]