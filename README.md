Terapia Alternativa

Una App de una empresa coordinadora entre medicos, pacientes y prepagas hecha con Python, usando el Django como framework

Utilizo una plantilla de bootstrap modificada y adaptada a la necesidad, en la cual renderizo los datos desde el backend, usando la herencia de padre a hijo para altenar las diferentes vistas que cree desde ahi.

models.py

En este archivo se encuentra el modelaje de datos de la tabla, Medicos, Pacientes y Prepagas.

forms.py

En este archivo se encuentra el formulario que hace envio de los datos ingresados al backend.

views.py

Aca encontraremos las vistas creadas y moldeadas para la navegacion de la web.

urls.py

Archivo donde esta la configuracion de rutas.

Inicio

En esta pagina podemos encontrar un viztaso general de la web, buscar medicos segun especialidades directamente de la db.

Medicos

Aca un medico puede ir y registrarse para trabajar con la organizacion.

Pacientes

Aca un paciente puede registrarse para solicitar un tratamiento.

Prepagas
Aca una prepaga puede registrarse para trabajar en conjunto con la organizacion y facilitar la atencion.

Authors
Matias Nicolas Gelaf
