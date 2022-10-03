from django.urls import path
from .views import home, krosovkaMakeAPI, singleAPI

app_name = 'api'

urlpatterns = [
    path('', home, name="home"),
    path('krosovka-api/', krosovkaMakeAPI),
    path('krosovka-api/<int:pk>/', singleAPI)

]