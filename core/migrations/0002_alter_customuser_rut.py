# Generated by Django 5.0.4 on 2024-05-06 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='rut',
            field=models.CharField(help_text='Ingrese el RUT sin puntos ni guión', max_length=20, unique=True),
        ),
    ]
