from django.urls import path
from App import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('medicos', views.medicos, name="Medicos"),
    path('pacientes', views.pacientes, name="Pacientes"),
    path('prepagas', views.prepagas, name="Prepagas"),
    path('medicoFormulario', views.medicos, name="Medico Formulario"),
    path('pacienteFormulario', views.pacientes, name="Paciente Formulario"),
    path('prepagaFormulario', views.prepagas, name="Prepaga Formulario"),
    path('buscar/', views.buscar),
      
]