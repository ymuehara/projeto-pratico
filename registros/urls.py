from django.urls import path, include
from registros import views
from .views import LogDetailView, LogCreateView, LogDeleteView, LogUpdateView, LogListAPIView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'logs', views.LogApiViewSet)

urlpatterns = [
    path('', views.central_errors, name='registros-home'),
    path('logincadastro/', views.login_cadastro, name='registros-login-cadastro'),
    path('detail/<int:pk>/', LogDetailView.as_view(), name='detail-central'),
    path('create/', LogCreateView.as_view(), name='log-create'),
    path('delete/<int:pk>/', LogDeleteView.as_view(), name='log-delete'),
    path('update/<int:pk>/', LogUpdateView.as_view(), name='log-update'),
    path('api/', include(router.urls), name='api-log'),
    path('api/search/', views.LogListAPIView.as_view(), name='api-search'),
    path('get_token/', obtain_auth_token),
]