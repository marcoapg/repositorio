from django.db import models

# Create your models here.

class estado(models.Model):
    estado_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural='estado'

class ciudad(models.Model):
    ciudad_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    norma=models.CharField(max_length=5)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural='ciudad'

class sede(models.Model):
    sede_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    capacidad=models.IntegerField()
    ciudad_id=models.ForeignKey(ciudad, on_delete=models.CASCADE,db_column='ciudad_id')
    estado_id=models.ForeignKey(estado, on_delete=models.CASCADE,db_column='estado_id')
    pais_id=models.ForeignKey("appCompeticion.pais",on_delete=models.CASCADE,db_column='pais_id')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural='sede'

class encuentro(models.Model):
    encuentro_id=models.BigAutoField(primary_key=True)
    equipo_local_id=models.ForeignKey("appEquipo.equipo", on_delete=models.CASCADE, related_name='equipo_local_id', db_column='equipo_local_id')
    equipo_visitante_id=models.ForeignKey("appEquipo.equipo", on_delete=models.CASCADE, related_name='equipo_visitante_id', db_column='equipo_visitante_id')
    resultado_general=models.CharField(max_length=1)
    resultado_equipo_a=models.IntegerField()
    resultado_equipo_b=models.IntegerField()
    sede_id=models.ForeignKey(sede,on_delete=models.CASCADE,db_column='sede_id')
    terna_arbitral_id=models.ForeignKey("appArbitro.terna_arbitral", on_delete=models.CASCADE,db_column='terna_arbitral_id')
    fecha=models.DateField()
    humedad=models.IntegerField()
    clima=models.IntegerField()
    estado_jugado=models.BooleanField()

    def __str__(self):
        return str(self.encuentro_id)
    

    class Meta:
        verbose_name_plural='encuentro'

class evento(models.Model):
    evento_id=models.BigAutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField()

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural='evento'

class evento_persona(models.Model):
    encuentro_evento_id=models.BigAutoField(primary_key=True)
    encuentro_id=models.ForeignKey(encuentro,on_delete=models.CASCADE,db_column='encuentro_id')
    evento_id=models.ForeignKey(evento,on_delete=models.CASCADE,db_column='evento_id')
    persona_id=models.ForeignKey("appContrato.persona",on_delete=models.CASCADE,db_column='persona_id')
    tiempo=models.IntegerField()

    def __str__(self):
        return str(self.encuentro_evento_id)

    class Meta:
        verbose_name_plural='evento_persona'

