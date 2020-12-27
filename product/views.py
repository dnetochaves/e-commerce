from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


class ListProduct(View):
    def get(*args, **kwargs):
        return HttpResponse('ListProduct')


class DetailsProduct(View):
     def get(*args, **kwargs):
        return HttpResponse('DetailsProduct')


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
