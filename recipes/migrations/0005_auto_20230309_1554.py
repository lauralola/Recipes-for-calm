# Generated by Django 3.2.17 on 2023-03-09 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20230223_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='title',
            new_name='header',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='featured_image',
            new_name='hero_image',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='excerpt',
            new_name='summary',
        ),
    ]
