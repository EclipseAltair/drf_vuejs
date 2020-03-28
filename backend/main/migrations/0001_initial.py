# Generated by Django 3.0.4 on 2020-03-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('year', models.PositiveSmallIntegerField()),
                ('volume', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]