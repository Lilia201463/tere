from django import forms
from apps.expediente.models import Expediente

class ExpedienteForm(forms.ModelForm):

	class Meta:
		model = Expediente

		fields = [
            'id_expediente',
            'nss_paciente', 
            'titulo',
            'fecha',
            'id_prueba',
            'id_cuestionario', 
            'observaciones',
		]
		labels={
		'id_expediente':'Número de expediente',
            'nss_paciente':'NSS', 
            'titulo':'Título',
            'fecha':'Fecha',
            'id_prueba':'Número de Prueba',
            'id_cuestionario':'Folio de cuestionario', 
            'observaciones':'Observaciones',

		}
		widgets = {

            'id_expediente':forms.Select(attrs={'class':'form-control'}),
            'nss_paciente':forms.Select(attrs={'class':'form-control'}), 
            'titulo':  forms.TextInput(attrs={'class':'form-control'}), 
            'fecha':  forms.SelectDateWidget(attrs={'class':'form-control'}, years=range(1995, 2100)),
            'id_prueba':forms.Select(attrs={'class':'form-control'}),
            'id_cuestionario':forms.Select(attrs={'class':'form-control'}), 
            'observaciones':  forms.TextInput(attrs={'class':'form-control'}), 
    		}