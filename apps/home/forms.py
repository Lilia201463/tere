from django import forms
from apps.home.models import Home

class HomeForm(forms.ModelForm):

    class Meta:
        model = Home

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
                  'apellido_paterno':'Primer apellido', 
                  'apellido_materno': 'Segundo apellido', 
                  'edad': 'Edad',
                  'sexo':'Sexo',
                  'residencia':'Localidad',
                  'even':'¿Se ha encontrado expuesto a alguno de los eventos se mencionan a continuación?',
                   'situacion':'En caso de haber tenido relaciones sexuales sin protección ¿bajo que circunstancia fue?',
                  'manifestaciones':'¿Cual de las siguientes manifestaciones clinicas ha presentado con mayor frecuencia?',
                  'infecciones':'¿Ha sido diagnosticado portador de alguna infección mencionada a continuación? (Indique cual) ',
                  'neoplasias':'Bajo supervisión médica ¿ha sido diagnosticado con alguno de los siguientes padecimientos? (Indique cual)',  



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
                  'even':  forms.RadioSelect(),
                  'situacion' :  forms.RadioSelect(),
                  'manifestaciones' :  forms.RadioSelect(),
                  'infecciones' :  forms.RadioSelect(),
                  'neoplasias' :  forms.RadioSelect(),
        }