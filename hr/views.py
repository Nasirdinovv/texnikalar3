from django.shortcuts import render, get_object_or_404
from hr.models import Workers

def all_hr(request):
    hamma_hodimlar = Workers.objects.all()
    return render(request, 'hodimlar_list.html', {'hamma_hodimlar': hamma_hodimlar})

def hr_detail(request, id):
    hodim = get_object_or_404(Workers, id=id)
    return render(request, 'hr_detail.html', {'hodim': hodim})