from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ListProduct.as_view(), name='list_product'),
    path('<slug>', views.DetailsProduct.as_view(), name='details_product'),
    path('add_cart/', views.AddCart.as_view(), name='add_cart'),
    path('remove_cart/', views.RemoveCart.as_view(), name='remove_cart'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('finish/', views.Finish.as_view(), name='finish'),
]
