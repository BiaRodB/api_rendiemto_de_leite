from django.db.models.query import QuerySet
from rest_framework import permissions
from leite.admin import *
from django.shortcuts import render
from rest_framework import serializers, viewsets, generics
from leite.models import *
from leite.serializer import *
from django.db.models import Sum
from django.http import JsonResponse
#from rest_framework.authentication import BaseAuthentication, BasicAuthentication
#from rest_framework.permissions import IsAuthenticated

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    #authentication_classes = [BaseAuthentication]
    #permission_classes = [IsAuthenticated]


class VacaViewSet(viewsets.ModelViewSet):
    queryset = Vaca.objects.all()
    serializer_class = VacaSerializer


class RendimentoViewSet(viewsets.ModelViewSet):
    queryset = Rendimento.objects.all()
    serializer_class = RendimentoSerializer




def somar_litros_vaca(request, vaca_id):
    rendimentos_vaca = Rendimento.objects.filter(vaca_id=vaca_id)
    total_litros_vaca = rendimentos_vaca.aggregate(Sum('litros'))['litros__sum']
    if total_litros_vaca is None:
        total_litros_vaca = 0
    return JsonResponse({'total_litros_vaca': total_litros_vaca})