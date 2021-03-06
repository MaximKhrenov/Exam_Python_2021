# Generated by Django 2.2.17 on 2021-01-19 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctorsApp', '0002_auto_20210119_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardPatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfVizit', models.DateField(verbose_name='Дата визита')),
                ('placeVizit', models.CharField(max_length=500, verbose_name='ФИО')),
                ('descVizit', models.TextField(verbose_name='Описание и назначения')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorsApp.Patient', verbose_name='Пациент')),
            ],
        ),
    ]
