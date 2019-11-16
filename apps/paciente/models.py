from django.db import models
from apps.medico.models import Medico
from django.core.validators import RegexValidator



class TelValidator(RegexValidator):
    regex = '^([0-9]{10})$'
    message = u'Telefono invalido'

class TextoValidator(RegexValidator):
    regex = '[A-Za-z]'
    message = u'Solo se admiten letras'

# Create your models here.
class Paciente(models.Model):
    nss_paciente = models.CharField(max_length=10, primary_key=True, unique=True)
    cedula_medico=models.ForeignKey(Medico, blank=False, related_name='medicos_rel', on_delete=models.SET(0))
    apellido_paterno = models.CharField(max_length=50, validators=[TextoValidator()])
    apellido_materno = models.CharField(max_length=50, validators=[TextoValidator()])
    nombres = models.CharField(max_length=50, validators=[TextoValidator()])
    fecha_nacimiento= models.DateField()
    SEXO_CHOICES=(
            ('Femenino', 'Femenino'),
            ('Masculino', 'Masculino'),
        )
    sexo=models.CharField(max_length =15, choices = SEXO_CHOICES)
    domicilio=models.TextField()
    correo_electronico=models.EmailField(max_length=255)
    telefono=models.CharField(max_length=20, validators=[TelValidator()])
    celular=models.CharField(max_length=20, validators=[TelValidator()])

    def __str__(self): 
       return '{} {} {} {}'.format(self.nss_paciente, self.apellido_paterno, self.apellido_materno, self.nombres)