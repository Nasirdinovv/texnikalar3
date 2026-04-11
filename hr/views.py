from django.shortcuts import render, get_object_or_404, redirect
from hr.models import Workers, Salary

def all_hr(request):
    hamma_hodimlar = Workers.objects.all()
    return render(request, 'hodimlar_list.html', {'hamma_hodimlar': hamma_hodimlar})

def hr_detail(request, id):
    hodim = get_object_or_404(Workers, id=id)
    return render(request, 'hr_detail.html', {'hodim': hodim})


def salary_delete(request, worker_id, salary_id):
    hodim = get_object_or_404(Workers, id=worker_id)
    salary = get_object_or_404(Salary, worker=hodim, id=salary_id)
    salary.delete()
    return redirect('hr_detail', id=hodim.id)


def update_salary_worker(request, worker_id, salary_id):
    hodim = get_object_or_404(Workers, id=worker_id)
    salary = get_object_or_404(Salary, worker=hodim, id=salary_id)

    if request.method == 'POST':
        month = request.POST.get("month")
        salary_sum = request.POST.get("salary_sum")

        salary.month = month
        salary.salary_sum = salary_sum
        salary.save()

        return redirect('hr_detail', id=hodim.id)

    return render(request, 'hr_update.html', {'salary': salary, 'hodim': hodim})
