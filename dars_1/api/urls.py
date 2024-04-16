from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("", views.CategoryList.as_view(), name="categories_list"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("login/", obtain_auth_token, name="login"),
    path("logout/", views.logout_user, name="logout_user"),
    path("signup/", views.user_register_view, name="user_register_view"),
    path("category/<str:pk>/", views.CategoryDetail.as_view(), name="category_detail"),
    path("products/", views.ProductList.as_view(), name="products_list"),
    path("product-detail/<int:id>/", views.ProductDetailView.as_view(), name="product_detail"),
]


