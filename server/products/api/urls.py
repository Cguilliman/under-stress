from django.urls import path
from . import views


urlpatterns = [
    path("products/create/", views.ProductCreateAPIView.as_view()),
    path("products/get/<int:product_id>/", views.ProductReceiveAPIView.as_view()),
    path("products/list/", views.ProductListAPIView.as_view()),
]
