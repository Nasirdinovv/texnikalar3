from django.urls import path
from .views import all_hr, hr_detail


urlpatterns = [
    path('', all_hr, name='all_hr'),
    path('<int:id>/', hr_detail, name='hr_detail'),
]
