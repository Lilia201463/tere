from django import forms
from apps.cuestionario.models import Cuestionario

class CuestionarioForm(forms.ModelForm):

    class Meta:
        model = Cuestionario

        fields = [
                  'id_cuestionario', 
                  'nss_paciente', 
                  'nombres', 
                  'apellido_paterno', 
                  'apellido_materno', 
                  'edad',
                  'sexo',
                  'residencia',
                  'even',
                  'situacion',
                  'manifestaciones',
                  'infecciones',
                  'neoplasias',

        ]
        labels={
                  'id_cuestionario': 'Folio', 
                  'nss_paciente':'NSS', 
                  'nombres':'Nombres', 
                  'apellido_paterno':'Primer Apellido',
                  'apellido_materno': 'Segundo Apellido',
                  'edad': 'Edad',
                  'sexo':'Sexo',
                  'residencia':'Localidad',
                  'even':'Eventos',
                   'situacion':'Situación',
                  'manifestaciones':'Manifestaciones',
                  'infecciones':'Infecciones',
                  'neoplasias':'Neoplasias',



        }
        widgets = {
                  'id_cuestionario' : forms.Select(attrs={'class':'form-control'}), 
                  'nss_paciente':  forms.TextInput(attrs={'class':'form-control'}), 
                  'nombres':  forms.TextInput(attrs={'class':'form-control'}), 
                  'apellido_paterno':  forms.TextInput(attrs={'class':'form-control'}), 
                  'apellido_materno':  forms.TextInput(attrs={'class':'form-control'}), 
                  'edad' : forms.Select(attrs={'class':'form-control'}),
                  'sexo' : forms.RadioSelect(),
                  'residencia' : forms.Select(attrs={'class':'form-control'}),
                  'eventos':  forms.RadioSelect(),
                  'situacion' :  forms.RadioSelect(),
                  'manifestaciones' :  forms.RadioSelect(),
                  'infecciones' :  forms.RadioSelect(),
                  'neoplasias' :  forms.RadioSelect(),
        }