# Generated by Django 5.0 on 2024-01-03 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
