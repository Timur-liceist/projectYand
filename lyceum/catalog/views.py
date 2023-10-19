from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, product_id):
    return HttpResponse("<body>Подробно элемент</body>")


def show_repath_positive_integer(request, product_id):
    return HttpResponse(f"<body>{product_id}</body>")


def positive_integer(request, product_id):
    return HttpResponse(f"<body>{product_id}</body>")
