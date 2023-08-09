
from django.shortcuts import render, redirect
from .models import Laboratorio, DirectorGeneral, Producto
from .forms import LaboratorioForm, DirectorGeneralForm, ProductoForm
from django.http import HttpResponse
from django.views.generic import TemplateView
import datetime

from django.http import HttpResponse , HttpResponseRedirect
from django.views.generic import TemplateView
import datetime
from .forms import InputForm, BoardsForm, RegistroUsuarioForm
from tokenize import PseudoExtras
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from django.utils import timezone
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http.response import JsonResponse

# Create your views here.
def aa0V(request):
    context = {}
    return render(request, '1.html', context)

def aa1V(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, '2.html', {'laboratorios': laboratorios})

def editar_laboratorio_view(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)

    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('/2')  
    else:
        form = LaboratorioForm(instance=laboratorio)

    return render(request, 'editlab.html', {'form': form})

def agregar_laboratorio_view(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('2')
    else:
        form = LaboratorioForm()
    
    return render(request, 'addlab.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/')

def eliminarlaboratorio_view(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id) 
    laboratorio.delete()
    messages.success(request, '¡Laboratorio Eliminado!') 
    return redirect('/2')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como : {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"Invalido username o password.")
        else:
            messages.error(request,"Invalido username o password.")

    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "log.html", context)

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente.")
            return HttpResponseRedirect('/')
    
        messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
    form = RegistroUsuarioForm()
    context = { "register_form" : form }
    return render(request, "registro.html", context)

