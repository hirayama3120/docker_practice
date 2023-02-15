"""django_api URL Configuration """
from django.urls import path, include

from django_api.views.order_view import OrderView

urlpatterns = [
    path('api/order/', OrderView.as_view()),
]