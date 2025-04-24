from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('price/', views.price, name='price'),
    path('tutor/', views.tutor, name='tutor'),
    path('why-ngs/', views.why_ngs, name='why-ngs'),
]
