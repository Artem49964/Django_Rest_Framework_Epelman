from django.urls import path

from .views import CarListView, RetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListView.as_view()),
    path('/<int:pk>', RetrieveUpdateDestroyView.as_view())
]