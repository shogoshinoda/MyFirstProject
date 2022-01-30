from django.http import HttpResponse
from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, 'error_handle/404.html', status=404)


# def server_error(request):
#     return render(request, 'error_handle/500.html', status=500)