# Generated by Django 4.2.7 on 2024-01-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditems',
            name='image',
            field=models.ImageField(default='', upload_to='menu/uploads'),
        ),
    ]
