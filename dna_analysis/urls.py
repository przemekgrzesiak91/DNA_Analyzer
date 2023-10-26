from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView  # new
from .views import SignUpView

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),  # new
    path('signup/', SignUpView.as_view(), name='signup'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('project_list', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_new, name='project_new'),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),
]