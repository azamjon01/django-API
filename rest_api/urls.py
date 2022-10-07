from django.urls import path
from .views import filterKrosovka, home, krosovkaMakeAPI, malumotDelete, malumotJoylash, malumotUpdate, singleAPI,krosovkaSearch

app_name = 'api'

urlpatterns = [
    path('', home, name="home"),
    path('krosovka-api/', krosovkaMakeAPI),
    path('krosovka-api/<int:pk>/', singleAPI),
    path('create/' , malumotJoylash),
    path('create/<int:pk>/', malumotUpdate),
    path('delete/<int:pk>/', malumotDelete),
    path('search/', krosovkaSearch),
    path('filter-bazm/', filterKrosovka )

]