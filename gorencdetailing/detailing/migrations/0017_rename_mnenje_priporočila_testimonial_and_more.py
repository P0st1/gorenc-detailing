# Generated by Django 4.2.6 on 2024-01-08 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detailing', '0016_priporočila_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='priporočila',
            old_name='mnenje',
            new_name='testimonial',
        ),
        migrations.RenameField(
            model_name='priporočila',
            old_name='avtor',
            new_name='user_name',
        ),
    ]
