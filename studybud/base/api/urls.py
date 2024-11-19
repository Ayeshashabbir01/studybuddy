from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.getRoutes, name='get_routes'),
    path('api/rooms/', views.getRooms, name='get_rooms'),
    path('api/rooms/<str:pk>/', views.getRoom, name='get_room'),
]
