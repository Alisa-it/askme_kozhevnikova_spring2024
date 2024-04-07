from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    path('ask/', views.ask, name='ask'),
    path('question/', views.question, name='question'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='signup'),
    path('tag/', views.tag, name='tag'),
    path('hot/', views.hot, name='hot'),

]
