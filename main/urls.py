from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='search'),
    path('personal-area/', views.personal_area, name='personal_area'),
    path('search/', views.index, name='search')
]
