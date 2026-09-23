from django.urls import path
from. import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('compare/', views.compare, name='compare'),
    path('wishlist/add/<int:id>/', views.add_wishlist, name='add_wishlist'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('price-alert/<int:id>/', views.price_alert, name='price_alert'),
]