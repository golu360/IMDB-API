# Generated by Django 3.0.8 on 2020-09-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=10),
        ),
    ]
