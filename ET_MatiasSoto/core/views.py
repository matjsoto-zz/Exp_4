from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm
# Create your views here.

def home(request):

    return render(request, 'home.html')

    
def form_crear(request):

    if request.method == 'POST': 

        persona_form = PersonaForm(request.POST)

        if persona_form.is_valid():

            persona_form.save()        #similar al insert de un modelo relacional 

            return redirect('home')

    else: 

        persona_form = PersonaForm()

    return render(request, 'core/form_crear.html', {'persona_form': persona_form})



def crud(request):

    persona = Persona.objects.all()

    return render(request, 'core/crud.html', context={'datos': persona})



def form_mod(request, id):

    persona = Persona.objects.get(rut=id)
    datos ={

        'form': PersonaForm(instance=persona)
    }
    
    if request.method == 'POST': 
        formulario = PersonaForm(data=request.POST, instance = persona)
        if formulario.is_valid: 
            formulario.save()
            return redirect('crud')
    return render(request, 'core/form_mod.html', datos)


def form_del(request,id):
    persona = Persona.objects.get(rut=id)
    persona.delete()
    return redirect('crud')


