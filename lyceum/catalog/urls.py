from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.PositiveIntConverter, "natural_integer")

urlpatterns = [
    path("<int:product_id>/", views.item_detail),
    path("", views.item_list),
    re_path(r"re/([1-9]\d*)/", views.show_repath_positive_integer),
    path("converter/<natural_integer:product_id>/", views.positive_integer),
]
