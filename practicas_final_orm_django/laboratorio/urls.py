from django.urls import path
from .views import registro_view, login_view, logout_view, \
    eliminarlaboratorio_view, agregar_laboratorio_view, \
    editar_laboratorio_view, \
    aa0V, aa1V

urlpatterns = [
    path('aa1/editlab/<int:id>/', editar_laboratorio_view, name='editar_laboratorio'),
    path('addlab/', agregar_laboratorio_view, name='agregar_laboratorio'),
    path('2/eliminarlaboratorio/<id>', eliminarlaboratorio_view, name='eliminarlaboratorio'),
    path('registro/', registro_view, name='registro'),
    path('log/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', aa0V, name ='aa0'),
    path('2/', aa1V, name ='aa1'),
]

