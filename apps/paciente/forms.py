from django import forms
from apps.paciente.models import Paciente

class PacienteForm(forms.ModelForm):

	class Meta:
		model = Paciente

		fields = [
        'nss_paciente', 
        'cedula_medico',
        'apellido_paterno',
        'apellido_materno', 
        'nombres', 
        'fecha_nacimiento',
        'sexo',
        'domicilio', 
        'correo_electronico',
        'telefono',
        'celular',
			
		]
		labels={
			'nss_paciente':'NSS', 
        'cedula_medico':'Medico asignado',
        'apellido_paterno':'Primer apellido',
        'apellido_materno':'Segundo apellido', 
        'nombres':'Nombre(s)', 
        'fecha_nacimiento':'Fecha de nacimiento',
        'sexo':'Sexo',
        'domicilio':'Domiciio', 
        'correo_electronico':'Correo electronico',
        'telefono':'Numero telefonico',
        'celular':'Celular',

		}
		widgets = {
        'nss_paciente':  forms.TextInput(attrs={'class':'form-control'}), 
        'cedula_medico': forms.Select(attrs={'class':'form-control'}),
        'apellido_paterno':  forms.TextInput(attrs={'class':'form-control'}),
        'apellido_materno':  forms.TextInput(attrs={'class':'form-control'}), 
        'nombres':  forms.TextInput(attrs={'class':'form-control'}), 
        'fecha_nacimiento':  forms.TextInput(attrs={'class':'datepicker'}),
        'sexo': forms.Select(attrs={'class':'form-control'}),
        'domicilio':  forms.TextInput(attrs={'class':'form-control'}), 
        'correo_electronico':  forms.TextInput(attrs={'class':'form-control'}),
        'telefono':  forms.TextInput(attrs={'class':'form-control'}),
        'celular':  forms.TextInput(attrs={'class':'form-control'}),
        }