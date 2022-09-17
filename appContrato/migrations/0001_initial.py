# Generated by Django 4.1.1 on 2022-09-17 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appCompeticion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipo_persona',
            fields=[
                ('tipo_persona_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('persona_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('alias', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=1)),
                ('fecha_nacimiento', models.DateField()),
                ('estatura', models.FloatField()),
                ('peso', models.FloatField()),
                ('estado', models.BooleanField()),
                ('pais_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appCompeticion.pais')),
                ('tipo_persona_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appContrato.tipo_persona')),
            ],
        ),
        migrations.CreateModel(
            name='contrato',
            fields=[
                ('contrato_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('valor', models.FloatField()),
                ('tipo_contrato', models.CharField(max_length=1)),
                ('estado', models.BooleanField()),
                ('persona_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appContrato.persona')),
            ],
        ),
    ]