# Generated by Django 5.1 on 2024-12-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='about/%Y/%m/%d'),
        ),
    ]
