# Generated by Django 5.2 on 2025-04-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asterapp', '0003_moviesinfo_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesinfo',
            name='poster',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
