# Generated by Django 4.2.6 on 2023-11-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrition_label',
            name='calories',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
