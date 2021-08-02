from django.shortcuts import render
from .models import UserCounter


def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def home_view(request):
    ip = visitor_ip_address(request)

    result = UserCounter.objects.filter(ip_address__contains=ip)
    if len(result) == 0:
        u_c = UserCounter.objects.create(ip_address=ip)
        u_c.save()
    else:
        pass

    user_count = UserCounter.objects.count()
    context = {
        'title': 'Geena Apparel',
        'user_count': user_count,

    }
    return render(request, 'geena_apparel/index.html', context)
