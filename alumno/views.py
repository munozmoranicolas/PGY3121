from django.shortcuts import render

# Create your views here.
def crud(request):
    return render(request,'alumno/crud.html')

def genero_list(request):
    return render(request,'alumno/genero_list.html')

def genero_add(request):
    return render(request,'alumno/genero_add.html')

def genero_edit(request):
    return render(request,'alumno/genero_edit.html')

def genero_del(request):
    return render(request,'alumno/genero_del.html')
