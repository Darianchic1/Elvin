# Generated by Django 4.1.7 on 2023-04-24 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atttent_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sky',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sky', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeRise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeRise', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeSet', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeWeather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('temp', models.IntegerField()),
                ('sky', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='TimeWeather6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('temp', models.IntegerField()),
                ('sky', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='DateWeather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('timeRise', models.TimeField()),
                ('timeSet', models.TimeField()),
                ('atttent_name', models.CharField(max_length=500)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeweather', to='my_app.city')),
                ('timeWeather', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeweather', to='my_app.timeweather')),
                ('timeWeather6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeweather6', to='my_app.timeweather6')),
            ],
        ),
    ]
