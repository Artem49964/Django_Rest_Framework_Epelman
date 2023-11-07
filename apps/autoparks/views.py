from django.http import Http404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer

from .filters import AutoParkFilter
from .models import AutoParkModel
from .serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all_with_cars()
    filterset_class = AutoParkFilter
    pagination_class = None

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)

        return (IsAdminUser(),)



class AutoParkRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()




class AutoParkCarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    model = CarModel

    def post(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        if not AutoParkModel.objects.filter(pk=pk).exists():
            raise Http404()
        serializer.save(auto_park_id=pk)
        return Response(serializer.data, status.HTTP_201_CREATED)
