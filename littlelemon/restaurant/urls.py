from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('menu/', views.menuview.as_view(), name='menuurl'),
    path('menu/<int:pk>/', views.singlemenuitemview.as_view(), name='singlemenuitemurl'),
    path('api-token-auth/', obtain_auth_token),
]
