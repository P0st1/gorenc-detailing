# Generated by Django 4.2.5 on 2023-10-09 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detailing', '0009_remove_avto_slike_avtoslike_avto'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontakt',
            name='delovni_cas',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
