# Generated by Django 4.1.7 on 2023-04-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QRApp', '0002_qrlink_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrlink',
            name='link',
            field=models.CharField(default='', max_length=400),
        ),
    ]
