from django.db import models


# Create your models here.


class Medico(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email = models.EmailField()


class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField()
    telefono = models.IntegerField()
    email= models.EmailField()


class Prepaga(models.Model):
    razon = models.CharField(max_length=100)
    cuit = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()
    
