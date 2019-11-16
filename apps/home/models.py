from django.db import models
from django.core.validators import RegexValidator



class TelValidator(RegexValidator):
    regex = '^([0-9]{10})$'
    message = u'Telefono invalido'

class TextoValidator(RegexValidator):
    regex = '[A-Za-z]'
    message = u'Solo se admiten letras'


# Create your models here.
class Home(models.Model):
    id_cuestionario = models.AutoField(primary_key=True)
    nss_paciente = models.CharField(max_length=11, unique=True, validators=[TelValidator()])
    nombres = models.CharField(max_length=50, validators=[TextoValidator()])
    apellido_paterno = models.CharField(max_length=50, validators=[TextoValidator()])
    apellido_materno = models.CharField(max_length=50, validators=[TextoValidator()])
    EDAD_CHOICES=(
            ('0.2', 'Menos de 1 año'),
            ('0.6', '1-4'),
            ('0.3', '5-9'),
            ('0.2', '10-14'),
            ('5.5', '15-19'),
            ('20.8', '20-24'),
            ('22.8', '25-29'),
            ('17.1', '30-34'),
            ('11.8', '35-39'),
            ('8.2', '40-44'),
            ('5.3', '45-49'),
            ('3.3', '50-54'),
            ('1.8', '55-59'),
            ('1', '60-64'),
            ('0.8', 'Mayor a 65'),
            
        )
    edad=models.CharField(max_length =15, choices = EDAD_CHOICES)
    SEXO_CHOICES=(
            ('21.9', 'Femenino'),
            ('78.1', 'Masculino'),
        )
    sexo=models.CharField(max_length =15, choices = SEXO_CHOICES)
    RESIDENCIA_CHOICES=(
            ('0.6', 'Aguas Calientes'),
            ('3.6', 'Baja California'),
            ('0.8', 'Baja California Sur'),
            ('1.3', 'Campeche'),
            ('1', 'Coahuila'),
            
            ('0.7', 'Colima'),
            ('4.2', 'Chiapas'),
            ('3.5', 'Chihuahua'),
            ('16.8', 'Ciudad de México'),
            ('0.6', 'Durango'),
            ('2.7', 'Guanajuato'),
            ('1.7', 'Guerrero'),
            ('1.2', 'Hidalgo'),
            ('3.6', 'Jalisco'),
            ('8.1', 'Estado de México'),
            ('1.5', 'Michoacan'),
            ('1.1', 'Morelos'),
            ('0.6', 'Nayarit'),
            ('4', 'Nuevo Leon'),
            ('3.4', 'Oaxaca'),
            ('4.5', 'Puebla'),
            ('1.7', 'Queretaro'),
            ('3.6', 'Quintana Roo'),
            ('1.5', 'San Luis Potosí'),
            ('1.6', 'Sinaloa'),
            ('1.6', 'Sonora'),
            ('3.8', 'Tabasco'),
            ('3.7', 'Tamaulipas'),
            ('0.5', 'Tlaxcala'),
            ('11.6', 'Veracruz'),
            ('4.0', 'Yucatan'),
            ('0.7', 'Zacatecas'),
            ('0.1', 'No especificado'),
        )
    residencia=models.CharField(max_length = 100, choices = RESIDENCIA_CHOICES)
    EVEN_CHOICES=(
            ('1.9', 'Mis padres han sido portadores del VIH'),
            ('1.4', 'He compartido jeringas para el uso de drogas'),
            ('1.8', 'He recibido una trasfusion sanguinea'),
            ('94.8', 'He mantenido relaciones sexuales sin proteccion'),

        )
    even=models.CharField(max_length =15, choices = EVEN_CHOICES, blank='true')
    SITUACION_CHOICES=(
            ('y1', 'Cuento con pareja sesxual estable'),
            ('y2', 'No tengo una pareja sexual estable'),
            ('y3', 'Fui victima de un abuso sexual'),
            ('y4', 'Soy trabajador(a) sexual'),

        )
    situacion=models.CharField(max_length =15, choices = SITUACION_CHOICES, blank='true')
    MANIFESTACIONES_CHOICES=(
            ('x1', 'Fiebre'),
            ('x2', 'Perdida de peso'),
            ('x3', 'Dificultades visuales'),
            ('x4', 'Afecciones respiratorias'),
            ('x5', 'Diarrea'),
            ('x6', 'Ulceras orales'),
            ('x7', 'Lesiones o erupciones cutaneas'),


        )
    manifestaciones=models.CharField(max_length =15, choices = MANIFESTACIONES_CHOICES, blank='true')
    INFECCIONES_CHOICES=(
            ('Z1', 'Candidiasis'),
            ('Z2', 'Citomegalovirus'),
            ('Z3', 'Cryptosporidiasis'),
            ('Z4', 'Hepatitis'),
            ('Z5', 'Herpes'),
            ('Z6', 'Salmonella'),
            ('Z7', 'Otra infeccion bacteriana'),


        )
    infecciones=models.CharField(max_length =15, choices = INFECCIONES_CHOICES, blank='true')
    NEOPLASIAS_CHOICES=(
            ('n1', 'Sarcoma de Kaposi'),
            ('n2', 'Linfoma cerebral primario'),
            ('n3', 'Enfermedad de Hodgkin'),
            ('n4', 'Cancer cervicouterno'),
            ('n5', 'Adenocarcinoma'),


        )
    neoplasias=models.CharField(max_length =15, choices = NEOPLASIAS_CHOICES, blank='true')




def __str__(self): 
       return '{} {} {}'.format(self.apellido_paterno, self.apellido_materno, self.nombres)

