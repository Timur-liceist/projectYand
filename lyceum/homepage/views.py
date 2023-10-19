from http import HTTPStatus

from django.http import HttpResponse


def home(request):
    return HttpResponse("<body>Главная</body>")


def show_endpoint_coffee(request):
    return HttpResponse("Я чайник", status=HTTPStatus.IM_A_TEAPOT)
