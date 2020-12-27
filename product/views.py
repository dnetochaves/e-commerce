from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from .models import Product


class ListProduct(ListView):
    model = Product
    template_name = 'product/list_product.html'
    context_object_name = 'products'
    paginate_by = 5


class DetailsProduct(DetailView):
     model = Product
     template_name = 'product/detail_product.html'
     context_object_name = 'product'
     slug_url_kwarg = 'slug'


class AddCart(View):
     def get(*args, **kwargs):
        return HttpResponse('AddCart')


class RemoveCart(View):
    def get(*args, **kwargs):
        return HttpResponse('RemoveCart')


class Cart(View):
    def get(*args, **kwargs):
        return HttpResponse('Cart')


class Finish(View):
    def get(*args, **kwargs):
        return HttpResponse('Finish')
