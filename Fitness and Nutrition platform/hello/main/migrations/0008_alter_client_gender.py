# Generated by Django 5.1 on 2024-09-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_owner_owner_usrname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]