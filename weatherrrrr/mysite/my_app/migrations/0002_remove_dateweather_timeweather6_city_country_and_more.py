# Generated by Django 4.1.7 on 2023-04-24 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dateweather',
            name='timeWeather6',
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='city', to='my_app.country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='country', to='my_app.continent'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TimeWeather6',
        ),
    ]
