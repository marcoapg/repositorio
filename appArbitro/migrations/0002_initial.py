# Generated by Django 4.1.1 on 2022-09-23 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appCompeticion', '0001_initial'),
        ('appArbitro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arbitro',
            name='pais_id',
            field=models.ForeignKey(db_column='pais_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.pais'),
        ),
    ]
