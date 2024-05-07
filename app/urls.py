from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('index/', views.Index, name='index'),
    path('login/', views.Login, name='login'),
    path('join_us/', views.Join_us, name='join_us'),
    path('profile/', views.Profile, name='profile'),
    path('save_application/', views.Save_Application, name='save_application'),
]
