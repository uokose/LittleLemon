from django.urls import path, include
from . import views

urlpatterns = [
    path('menu/',views.menuview.as_view(), name='menuurl' ),
    path('menu/<int:pk>/',views.singlemenuitemview.as_view(), name='singlemenuitemurl' ),
]
