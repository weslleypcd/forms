from django.urls import path
from .views import aluno_preenche

urlpatterns = [
    path('preenche/', aluno_preenche, name='preenche'),
]

