from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),

    # Вбудовані views для автентифікації
    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]