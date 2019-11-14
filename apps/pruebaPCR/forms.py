from django import forms
from apps.pruebaPCR.models import Prueba_PCR

class PruebaForm(forms.ModelForm):

	class Meta:
		model = Prueba_PCR

		fields = [
        'id_prueba',
        'nss_paciente',
        'cadena_PCR',
        'resultado',
        
			
		]
		labels={
		'id_prueba':'Número de prueba',
        'nss_paciente': 'NSS',
        'cadena_PCR':'Cadena PCR',
        'resultado':'Resultado',

		}
		widgets = {

        'id_prueba':forms.TextInput(attrs={'class':'form-control'}), 
        'nss_paciente': forms.Select(attrs={'class':'form-control'}),
        'cadena_PCR':forms.TextInput(attrs={'class':'form-control'}), 
        'resultado':forms.TextInput(attrs={'class':'form-control'}), 


   
			
		}