# Generated by Django 3.2.17 on 2023-02-23 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-updated_on']},
        ),
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.CharField(choices=[('Meditation', 'Meditation'), ('Yoga', 'Yoga'), ('Technology', 'Technology'), ('Moment', 'Moment')], default='Meditation', max_length=50),
        ),
    ]
