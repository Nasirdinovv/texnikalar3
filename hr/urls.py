from django.urls import path
from .views import all_hr


urlpatterns = [
    path('', all_hr, name='all_hr'),
]
