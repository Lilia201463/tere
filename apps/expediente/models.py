from django.db import models
from apps.paciente.models import Paciente
from apps.pruebaPCR.models import Prueba_PCR
from apps.home.models import Home
from django.core.validators import RegexValidator



class TelValidator(RegexValidator):
    regex = '^([0-9]{10})$'
    message = u'Telefono invalido'

class TextoValidator(RegexValidator):
    regex = '[A-Za-z]'
    message = u'Solo se admiten letras'

class Expediente(models.Model):
    id_expediente=models.AutoField(primary_key=True)
    nss_paciente = models.OneToOneField(Paciente, null=True, blank=False, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, blank=True, validators=[TextoValidator()])
    fecha = models.DateField()
    id_prueba = models.ForeignKey(Prueba_PCR, null=True, blank=False, on_delete=models.SET(0),related_name='pruebas_rel')
    id_cuestionario = models.ForeignKey(Home, null=True, blank=False, on_delete=models.SET(0),related_name='cuestionarios_rel')
    observaciones=models.TextField(blank=True)



    def __str__(self): 
       return '{}'.format(self.id_expediente)