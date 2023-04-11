from django.shortcuts import render, redirect
from .models import *

def home(request):
    pessoas = Pessoa.objects.all()

    context = {
        'pessoa':pessoas,
    }
    return render(request, "index.html",context)



def salvar(request):
    if request.method == 'POST':
        nome = request.POST.get("nome")
        nivel = request.POST.get("nivel")
        print(f'>>>>{nivel}')
        pessoa = Pessoa.objects.create(nome=nome, importancia=nivel)        
        pessoa.save() 
        
    return redirect("core:home")



def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})


def update(request, id):
    vnome = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.save()
    return redirect("core:home")

def delete(request, id):
    pessoa = Pessoa.objects.filter(id=id)
    pessoa.delete()
    return redirect("core:home")

