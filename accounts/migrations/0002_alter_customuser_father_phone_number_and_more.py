# Generated by Django 5.2.1 on 2025-06-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='father_phone_number',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
