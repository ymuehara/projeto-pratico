from django.urls import path
from registros import views
from .views import LogDetailView

urlpatterns = [
    path('', views.central_errors, name='registros-home'),
    path('logincadastro/', views.login_cadastro, name='registros-login-cadastro'),
    path('detail/<int:pk>/', LogDetailView.as_view(), name='detail-central'),
]