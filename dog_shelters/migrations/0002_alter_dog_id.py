# Generated by Django 5.0.6 on 2024-05-07 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
