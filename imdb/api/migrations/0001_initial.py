# Generated by Django 3.0.8 on 2020-09-25 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No Name Available', max_length=1000)),
                ('year', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=0)),
                ('certificate', models.CharField(default='None', max_length=10)),
                ('duration', models.IntegerField(default=0)),
                ('genre', models.CharField(default='None', max_length=50)),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=1)),
                ('description', models.CharField(default='No Description Available', max_length=2000)),
            ],
        ),
    ]
