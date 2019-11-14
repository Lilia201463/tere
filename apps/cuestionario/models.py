from django.db import models

# Create your models here.
class Cuestionario(models.Model):
    id_cuestionario = models.AutoField(primary_key=True)
    nss_paciente = models.CharField(max_length=11, unique=True)
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    EDAD_CHOICES=(
            ('Menos de 1 año', 'Menos de 1 año'),
            ('1-4', '1-4'),
            ('5-9', '5-9'),
            ('10-14', '10-14'),
            ('15-19', '15-19'),
            ('20-24', '20-24'),
            ('25-29', '25-29'),
            ('30-34', '30-34'),
            ('35-39', '35-39'),
            ('40-44', '40-44'),
            ('45-49', '45-49'),
            ('50-54', '50-54'),
            ('55-59', '55-59'),
            ('60-64', '60-64'),
            ('Mayor a 65', 'Mayor a 65'),
            
        )
    edad=models.CharField(max_length =15, choices = EDAD_CHOICES)
    SEXO_CHOICES=(
            ('Femenino', 'Femenino'),
            ('Masculino', 'Masculino'),
        )
    sexo=models.CharField(max_length =15, choices = SEXO_CHOICES)
    domicilio=models.TextField()
    ESTADOCIVIL_CHOICES=(
            ('Casado', 'Casado'),
            ('Soltero', 'Sotero'),
            ('Viudo', 'Viudo'),
            ('Divorceado', 'Divorciado'),
            ('Union libre', 'Union Libre'),
        )
    estado_civil=models.CharField(max_length =15, choices = ESTADOCIVIL_CHOICES)
    RESIDENCIA_CHOICES=(
            ('Aguas Calientes', 'Aguas Calientes'),
            ('Baja California', 'Baja California'),
            ('Baja California Sur', 'Baja California Sur'),
            ('Campeche', 'Campeche'),
            ('Coahuila', 'Coahuila'),
            ('Colima', 'Colima'),
            ('Chiapas', 'Chiapas'),
            ('Chihuahua', 'Chihuahua'),
            ('Ciudad de México', 'Ciudad de México'),
            ('Durango', 'Durango'),
            ('Guanajuato', 'Guanajuato'),
            ('Guerrero', 'Guerrero'),
            ('Hidalgo', 'Hidalgo'),
            ('Jalisco', 'Jalisco'),
            ('Estado de México', 'Estado de México'),
            ('Michoacan', 'Michoacan'),
            ('Morelos', 'Morelos'),
            ('Nayarit', 'Nayarit'),
            ('Nuevo Leon', 'Nuevo Leon'),
            ('Oaxaca', 'Oaxaca'),
            ('Puebla', 'Puebla'),
            ('Queretaro', 'Queretaro'),
            ('Quintana Roo', 'Quintana Roo'),
            ('San Luis Potosí', 'San Luis Potosí'),
            ('Sinaloa', 'Sinaloa'),
            ('Sonora', 'Sonora'),
            ('Tabasco', 'Tabasco'),
            ('Tamaulipas', 'Tamaulipas'),
            ('Tlaxcala', 'Tlaxcala'),
            ('Veracruz', 'Veracruz'),
            ('Yucatan', 'Yucatan'),
            ('Zacatecas', 'Zacatecas'),
            ('No especificado', 'No especificado'),
        )
    residencia=models.CharField(max_length = 100, choices = RESIDENCIA_CHOICES)
    celular=models.CharField(max_length=20)



def __str__(self): 
       return '{} {} {}'.format(self.id_cuestionario, self.apellido_paterno, self.nombres)