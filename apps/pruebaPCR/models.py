from django.db import models
from apps.paciente.models import Paciente
# Create your models here.

class Prueba_PCR(models.Model):
	id_prueba=models.AutoField(primary_key=True)
	nss_paciente = models.OneToOneField(Paciente, null=True, blank=False, on_delete=models.CASCADE)
	cadena_PCR= models.TextField()
	resultado= models.IntegerField(blank=True)


def __str__(self): 
       return '{} {}'.format(self.id_prueba, self.nss_paciente)