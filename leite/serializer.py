from django.db import models
from django.db.models import fields
from rest_framework import serializers
from leite.models import *


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class VacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaca
        fields = '__all__'


class RendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rendimento
        fields = '__all__'


