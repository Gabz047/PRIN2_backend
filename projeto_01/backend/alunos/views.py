from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Estado, Cidade, Aluno
from .serializers import EstadoSerializer, CidadeSerializer, AlunoSerializer
# Create your views here.

class EstadoViewset(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewset(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class AlunoViewset(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


