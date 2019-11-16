from django.db import models
from apps.paciente.models import Paciente
from django.core.validators import RegexValidator

class NumValidator(RegexValidator):
    regex = '^([0-9])$'
    message = u'Telefono invalido'

class TelValidator(RegexValidator):
    regex = '^([0-9]{8})$'
    message = u'Telefono invalido'

class TextoValidator(RegexValidator):
    regex = '[A-Za-z]'
    message = u'Solo se admiten letras'
# Create your models here.

class Prueba_PCR(models.Model):
	id_prueba=models.AutoField(primary_key=True)
	nss_paciente = models.OneToOneField(Paciente, null=True, blank=False, on_delete=models.CASCADE)
	cadena_PCR= models.CharField(max_length=8, validators=[TextoValidator()])
	resultado= models.IntegerField(blank=True, validators=[NumValidator()])


def __str__(self): 
       return '{} {}'.format(self.id_prueba, self.nss_paciente)