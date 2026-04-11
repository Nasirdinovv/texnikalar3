from django.urls import path
from .views import all_hr, hr_detail, salary_delete, update_salary_worker


urlpatterns = [
    path('', all_hr, name='all_hr'),
    path('<int:id>/', hr_detail, name='hr_detail'),
    path('salary-delete/<int:worker_id>/<int:salary_id>/', salary_delete, name='salary_delete'),
    path('salary-update/<int:worker_id>/<int:salary_id>/', update_salary_worker, name='salary_update'),
]
