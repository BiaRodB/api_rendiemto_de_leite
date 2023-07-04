from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from leite.views import *

router = routers.DefaultRouter()
router.register('pessoa', PessoaViewSet, basename='Pessoas')
router.register('vaca', VacaViewSet, basename='Vacas')
router.register('rendimento', RendimentoViewSet, basename='Rendimentos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
 #   path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
  #  path('curso/<int:pk>/matriculas/', ListaAlunosMatriculaCurso.as_view())
]