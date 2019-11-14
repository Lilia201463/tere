from django import forms
from apps.medico.models import Medico

class MedicoForm(forms.ModelForm):

    class Meta:
        model = Medico

        fields = [
                  
                  'cedula_medico',
                  'apellido_paterno',
                  'apellido_materno',
                  'nombres',
                  'fecha_nacimiento',
                  'sexo',
                  'domicilio', 
                  'especialidad',
                  'celular',

        ]
        labels={
                  'cedula_medico': 'Número de Cédula',
                  'apellido_paterno':'Primer Apellido',
                  'apellido_materno': 'Segundo Apellido',
                  'nombres': 'Nombre(s)',
                  'fecha_nacimiento': 'Fecha de Nacimiento',
                  'sexo':'Sexo',
                  'domicilio':'Domicilio',
                  'especialidad':'Especialidad',
                  'celular':'Número de Celular',

        }
        widgets = {
                  'cedula_medico' : forms.TextInput(attrs={'class':'form-control'}),
                  'apellido_paterno':  forms.TextInput(attrs={'class':'form-control'}), 
                  'apellido_materno':  forms.TextInput(attrs={'class':'form-control'}), 
                  'nombres':  forms.TextInput(attrs={'class':'form-control'}), 
                  'fecha_nacimiento':  forms.TextInput(attrs={'class':'form-control'}),
                  'sexo' : forms.Select(attrs={'class':'form-control'}),
                  'domicilio':  forms.TextInput(attrs={'class':'form-control'}),
                  'especialidad' : forms.TextInput(attrs={'class':'form-control'}),  
                  'celular':  forms.TextInput(attrs={'class':'form-control'}),
        }