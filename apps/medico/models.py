from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator



class TelValidator(RegexValidator):
    regex = '^([0-9]{10})$'
    message = u'Telefono invalido'

class TextoValidator(RegexValidator):
    regex = '[A-Za-z]'
    message = u'Solo se admiten letras'


# Create your models here.
class Medico(models.Model):
    cedula_medico = models.CharField(max_length=10, primary_key=True, unique=True)
    apellido_paterno = models.CharField(max_length=50, validators=[TextoValidator()])
    apellido_materno = models.CharField(max_length=50, validators=[TextoValidator()])
    nombres = models.CharField(max_length=50, validators=[TextoValidator()])
    fecha_nacimiento= models.DateField()
    fecha_registro=datetime.now()
    SEXO_CHOICES=(
            ('Femenino', 'Femenino'),
            ('Masculino', 'Masculino'),
        )
    sexo=models.CharField(max_length =15, choices = SEXO_CHOICES)
    domicilio=models.TextField()
    especialidad=models.CharField(max_length=20, validators=[TextoValidator()])
    celular=models.CharField(max_length=20, validators=[TelValidator()])


                  
    def __str__(self): 
       return '{} {} {}'.format(self.cedula_medico, self.apellido_paterno,  self.nombres)