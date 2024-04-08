from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    path('ask/', views.ask, name='ask'),
    path('question/<int:question_id>', views.question, name='question'),
    path('login/', views.login, name='login'),
    path('signup/', views.register, name='signup'),
    path('tag/<str:tag_name>', views.tag, name='tag'),
    path('hot/', views.hot, name='hot'),
]
