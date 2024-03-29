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
                  'domicilio',
                  'estado_civil',
                  'residencia',
                  'celular',

        ]
        labels={
                  'id_cuestionario': 'Folio', 
                  'nss_paciente':'NSS', 
                  'nombres':'Nombres', 
                  'apellido_paterno':'Primer apellido', 
                  'apellido_materno': 'Segundo apellido', 
                  'edad': 'Edad',
                  'sexo':'Sexo',
                  'domicilio':'Domicilio',
                  'estado_civil':'Estado civil',
                  'residencia':'Localidad',
                  'celular':'Numero telefonico',

        }
        widgets = {
                  'id_cuestionario' : forms.Select(attrs={'class':'form-control'}), 
                  'nss_paciente':  forms.TextInput(attrs={'class':'form-control'}), 
                  'nombres':  forms.TextInput(attrs={'class':'form-control'}), 
                  'apellido_paterno':  forms.TextInput(attrs={'class':'form-control'}), 
                  'apellido_materno':  forms.TextInput(attrs={'class':'form-control'}), 
                  'edad' : forms.Select(attrs={'class':'form-control'}),
                  'sexo' : forms.Select(attrs={'class':'form-control'}),
                  'domicilio':  forms.TextInput(attrs={'class':'form-control'}),
                  'estado_civil' : forms.Select(attrs={'class':'form-control'}),
                  'residencia' : forms.Select(attrs={'class':'form-control'}),
                  'celular':  forms.TextInput(attrs={'class':'form-control'}),
        }