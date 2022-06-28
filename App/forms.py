from django import forms


class MedicoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=30)
    telefono = forms.IntegerField()
    email = forms.EmailField()


class PacienteFormulario(forms.Form):   
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    fechaDeNacimiento = forms.DateField()
    telefono = forms.IntegerField()
    email= forms.EmailField()

class PrepagaFormulario(forms.Form):

    razon = forms.CharField(max_length=100)
    cuit = forms.IntegerField()
    telefono = forms.IntegerField()
    email = forms.EmailField()