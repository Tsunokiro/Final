from django.shortcuts import render, HttpResponse, redirect
from Finalapp.models import Curso
from Finalapp.models import Carrera
from django.contrib import messages


def index(request):
    return render(request, 'index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Examen Final'
    })

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html',{
        'cursos': cursos,
        'titulo': 'Listado de Cursos'
    })

def crear_curso(request):
    return render(request, 'crear_curso.html',{
        'titulo': 'Agregar Curso'
    })

def eliminar_curso(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('cursos')

def save_curso(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        horas = request.POST['horas']
        credito = request.POST['credito']
        estado = request.POST['estado']
 
        curso = Curso(
            codigo = codigo,
            nombre = nombre,
            horas = horas,
            creditos = credito,
            estado = estado
        )
        curso.save()
        # Crear un mensaje flash (Sesión que solo se muestra 1 vez)
        messages.success(request, f'Se agregó correctamente el curso {curso.id}')
        return redirect('cursos')
    else:
        return HttpResponse("<h2>No se ha podido registrar el curso</h2>")

def carreras(request):
    carreras = Carrera.objects.all()
    return render(request, 'carreras.html', {
        'carreras': carreras,
        'titulo': 'Listado de Carreras'
    })

def crear_carrera(request):
    return render(request, 'crear_carrera.html',{
        'titulo': 'Crear Carrera'
    })

def save_carrera(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nombre_corto = request.POST['nombre_corto']
        imagen = request.POST['imagen']
        estado = request.POST['estado']
 
        carrera = Carrera(
            nombre = nombre,
            nombre_corto = nombre_corto,
            imagen = imagen,
            estado = estado
        )
        carrera.save()
        messages.success(request, f'Se agregó correctamente la carrera {carrera.id}')
        return redirect('carreras')
    else:
        return HttpResponse("<h2>No se ha podido registrar la carrera</h2>")

def eliminar_carrera(request, id):
    carrera = Carrera.objects.get(pk=id)
    carrera.delete()
    return redirect('carreras')
