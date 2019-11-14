from django.db import models

# Create your models here.
class Medico(models.Model):
    cedula_medico = models.CharField(max_length=10, primary_key=True, unique=True)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    fecha_nacimiento= models.DateField()
    SEXO_CHOICES=(
            ('Femenino', 'Femenino'),
            ('Masculino', 'Masculino'),
        )
    sexo=models.CharField(max_length =15, choices = SEXO_CHOICES)
    domicilio=models.TextField()
    especialidad=models.CharField(max_length=20)
    celular=models.CharField(max_length=20)
                  
    def __str__(self): 
       return '{} {} {}'.format(self.cedula_medico, self.apellido_paterno,  self.nombres)