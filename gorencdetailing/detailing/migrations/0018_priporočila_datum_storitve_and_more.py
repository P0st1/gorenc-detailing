# Generated by Django 4.2.6 on 2024-01-08 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detailing', '0017_rename_mnenje_priporočila_testimonial_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='priporočila',
            name='datum_storitve',
            field=models.DateField(null=True, verbose_name='Datum storitve'),
        ),
        migrations.AddField(
            model_name='priporočila',
            name='type_of_service',
            field=models.CharField(max_length=100, null=True, verbose_name='Vrsta storitve'),
        ),
    ]
