from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductList.as_view(), name='products'),
    path('load-products/', views.load_products, name="load_products"),
]
