from django.urls import path

from .views import AutoParkCarListCreateView, AutoParkListCreateView, AutoParkRetrieveUpdateDestroyApiView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyApiView.as_view()),
    path('/<int:pk>/cars', AutoParkCarListCreateView.as_view()),
]

