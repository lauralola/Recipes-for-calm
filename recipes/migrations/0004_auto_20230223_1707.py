# Generated by Django 3.2.17 on 2023-02-23 17:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0003_alter_recipe_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='like_count',
            field=models.BigIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='recipe_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
