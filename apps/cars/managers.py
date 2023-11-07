from django.db import models


class CarManager(models.Manager):
    def get_cars_by_auto_park_id(self, pk):
        return self.filter(auto_park_id=pk)
    

    def get_only_kia(self):
        return self.filter(brand='KIA')