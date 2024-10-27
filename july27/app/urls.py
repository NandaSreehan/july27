from django.urls import path
from app import views
urlpatterns=[
    path('prime',views.prime, name='primeNumbers')

]