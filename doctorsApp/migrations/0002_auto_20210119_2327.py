# Generated by Django 2.2.17 on 2021-01-19 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctorsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Врач'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='adress',
            field=models.CharField(max_length=500, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=200, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(max_length=200, verbose_name='Пол'),
        ),
    ]
