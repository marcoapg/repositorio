# Generated by Django 4.1.1 on 2022-09-23 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appEquipo', '0001_initial'),
        ('appCompeticion', '0001_initial'),
        ('appArbitro', '0002_initial'),
        ('appContrato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ciudad',
            fields=[
                ('ciudad_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('norma', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'ciudad',
            },
        ),
        migrations.CreateModel(
            name='encuentro',
            fields=[
                ('encuentro_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('resultado_general', models.CharField(max_length=1)),
                ('resultado_equipo_a', models.IntegerField()),
                ('resultado_equipo_b', models.IntegerField()),
                ('fecha', models.DateField()),
                ('humedad', models.IntegerField()),
                ('clima', models.IntegerField()),
                ('estado_jugado', models.BooleanField()),
                ('equipo_local_id', models.ForeignKey(db_column='equipo_local_id', on_delete=django.db.models.deletion.CASCADE, related_name='equipo_local_id', to='appEquipo.equipo')),
                ('equipo_visitante_id', models.ForeignKey(db_column='equipo_visitante_id', on_delete=django.db.models.deletion.CASCADE, related_name='equipo_visitante_id', to='appEquipo.equipo')),
            ],
            options={
                'verbose_name_plural': 'encuentro',
            },
        ),
        migrations.CreateModel(
            name='estado',
            fields=[
                ('estado_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'estado',
            },
        ),
        migrations.CreateModel(
            name='evento',
            fields=[
                ('evento_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
                ('estado', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'evento',
            },
        ),
        migrations.CreateModel(
            name='sede',
            fields=[
                ('sede_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('capacidad', models.IntegerField()),
                ('ciudad_id', models.ForeignKey(db_column='ciudad_id', on_delete=django.db.models.deletion.CASCADE, to='appPartido.ciudad')),
                ('estado_id', models.ForeignKey(db_column='estado_id', on_delete=django.db.models.deletion.CASCADE, to='appPartido.estado')),
                ('pais_id', models.ForeignKey(db_column='pais_id', on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.pais')),
            ],
            options={
                'verbose_name_plural': 'sede',
            },
        ),
        migrations.CreateModel(
            name='evento_persona',
            fields=[
                ('encuentro_evento_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tiempo', models.IntegerField()),
                ('encuentro_id', models.ForeignKey(db_column='encuentro_id', on_delete=django.db.models.deletion.CASCADE, to='appPartido.encuentro')),
                ('evento_id', models.ForeignKey(db_column='evento_id', on_delete=django.db.models.deletion.CASCADE, to='appPartido.evento')),
                ('persona_id', models.ForeignKey(db_column='persona_id', on_delete=django.db.models.deletion.CASCADE, to='appContrato.persona')),
            ],
            options={
                'verbose_name_plural': 'evento_persona',
            },
        ),
        migrations.AddField(
            model_name='encuentro',
            name='sede_id',
            field=models.ForeignKey(db_column='sede_id', on_delete=django.db.models.deletion.CASCADE, to='appPartido.sede'),
        ),
        migrations.AddField(
            model_name='encuentro',
            name='terna_arbitral_id',
            field=models.ForeignKey(db_column='terna_arbitral_id', on_delete=django.db.models.deletion.CASCADE, to='appArbitro.terna_arbitral'),
        ),
    ]
