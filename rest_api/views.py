from django.shortcuts import render
from .serializers import KrosovkaAPI
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .models import *
from rest_framework import generics
from rest_framework import filters

def home(request):
    return render(request, 'home.html')

# API tolq chiqarish
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def krosovkaMakeAPI(request):
    krosovka = Krosovka.objects.all()
    serializer = KrosovkaAPI(krosovka, many=True)
    return Response(serializer.data)

# api ni id orqali (alohida, ALOHIDA) CHIQARISH
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def singleAPI(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializer = KrosovkaAPI(krosovka, many=False)
    return Response(serializer.data)

# post joylash (malumot joylash)    
@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def malumotJoylash(request):
    krosovka = Krosovka.objects.get(id)
    serializer = KrosovkaAPI(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

  
# post joylash Update qilish    
@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def malumotUpdate(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializer = KrosovkaAPI(instance=krosovka, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

# post delet
# 
# post qilish
@api_view(["DELETE"])
@permission_classes((permissions.AllowAny, ))
def malumotDelete(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    

    
    return Response('Mufaqiyatli ochirildi')    

# Rest API FILTER 
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))

def filterKrosovka(request):
    filter = Krosovka.objects.filter(turi='BAZM')
    serializer = KrosovkaAPI(filter, many=True)
    return Response(serializer.data)
# SEARCH API
class KrosovkaSearchAPI(generics.ListAPIView):
    queryset = Krosovka.objects.all()
    serializer_class = KrosovkaAPI
    filter_backends = [filters.SearchFilter]
    search_fields = ['brand', 'color']

krosovkaSearch = KrosovkaSearchAPI.as_view()    