# Generated by Django 4.1.1 on 2022-09-17 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appEquipo', '0002_initial'),
        ('appCompeticion', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competicion',
            name='tipo_competicion_id',
            field=models.ForeignKey(db_column='tipo_competicion_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.tipo_competicion'),
        ),
        migrations.AlterField(
            model_name='detalle_grupo',
            name='competicion_id',
            field=models.ForeignKey(db_column='competicion_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.competicion'),
        ),
        migrations.AlterField(
            model_name='detalle_grupo',
            name='equipo_id',
            field=models.ForeignKey(db_column='equipo_id', on_delete=django.db.models.deletion.CASCADE, to='appEquipo.equipo'),
        ),
        migrations.AlterField(
            model_name='detalle_grupo',
            name='grupo_id',
            field=models.ForeignKey(db_column='grupo_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.grupo'),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='competicion_id',
            field=models.ForeignKey(db_column='competicion_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.competicion'),
        ),
        migrations.AlterField(
            model_name='tabla',
            name='equipo_id',
            field=models.ForeignKey(db_column='equipo_id', on_delete=django.db.models.deletion.CASCADE, to='appEquipo.equipo'),
        ),
    ]