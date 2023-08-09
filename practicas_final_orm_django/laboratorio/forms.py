
from django import forms
from .models import BoardsModel
from .models import Laboratorio, DirectorGeneral, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class InputForm(forms.Form):
    nombres = forms.CharField(max_length = 200)
    apellidos = forms.CharField(max_length = 200)
    prioridad = forms.IntegerField(min_value=1, max_value=3)
    contrasenna = forms.CharField(widget = forms.PasswordInput())

class BoardsForm(forms.ModelForm):
    class Meta:
        model = BoardsModel
        fields = "__all__"
        

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistroUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
                user.save()
        return user
    
class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']

class DirectorGeneralForm(forms.ModelForm):
    class Meta:
        model = DirectorGeneral
        fields = ['nombre', 'especialidad']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta']
