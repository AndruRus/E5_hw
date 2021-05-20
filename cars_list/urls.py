from django.contrib import admin
from django.urls import path
from cars.views import CarsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarsListView.as_view(), name='cars-list')
]
