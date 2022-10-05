from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.pagination import PageNumberPagination 
from .models import *
from .serializers import AnimalsSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
# Create your views here.


class AnimalsAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000
    

class AnimalsApiList(generics.ListCreateAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = AnimalsAPIListPagination

class AnimalsApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalsSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsOwnerOrReadOnly,)
    

class AnimalsApiDestroy(generics.RetrieveDestroyAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalsSerializer
    #permission_classes = (IsAdminUser,)
    permission_classes = (IsAdminOrReadOnly,)