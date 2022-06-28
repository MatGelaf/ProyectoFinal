from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from App.models import Medico, Paciente, Prepaga
from App.forms import MedicoFormulario, PacienteFormulario, PrepagaFormulario

# Create your views here.


def inicio(request):

      return render(request, "App/inicio.html")


def medicos(request):

      if request.method == 'POST':

            miFormulario = MedicoFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data
                  print(informacion)
                  medico = Medico (nombre=informacion['nombre'], apellido=informacion['apellido'], especialidad=informacion['especialidad'], telefono=informacion['telefono'], email=informacion['email']) 

                  medico.save()

                  return render(request, "App/inicio.html")

      else: 

            miFormulario= MedicoFormulario()

      return render(request, "App/medicos.html", {"miFormulario":miFormulario})


def pacientes(request):

      if request.method == 'POST':

            miFormulario = PacienteFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  paciente = Paciente(nombre=informacion['nombre'], apellido=informacion['apellido'], fechaDeNacimiento=informacion['fechaDeNacimiento'], telefono=informacion['telefono'], email=informacion['email']) 

                  paciente.save()

                  return render(request, "App/inicio.html")

      else: 

            miFormulario= PacienteFormulario()

      return render(request, "App/pacientes.html", {"miFormulario":miFormulario})


def prepagas(request):

      if request.method == 'POST':

            miFormulario = PrepagaFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  prepaga = Prepaga(razon=informacion['razon'], cuit=informacion['cuit'], telefono=informacion['telefono'], email=informacion['email']) 

                  prepaga.save()

                  return render(request, "App/inicio.html")

      else: 

            miFormulario= PrepagaFormulario()

      return render(request, "App/prepagas.html", {"miFormulario":miFormulario})


def buscar(request):

      if  request.GET["especialidad"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            especialidad = request.GET['especialidad'] 
            print(especialidad)
            medicos = Medico.objects.filter(especialidad__icontains=especialidad)
            print(medicos)
            return render(request, "App/inicio.html", {"medicos":medicos, "especialidad":especialidad})

      else: 

	      respuesta = "No enviaste datos"
          
      return render(request,"App/inicio.html", {"respuesta":respuesta})