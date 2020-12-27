from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


class Pay(View):
    def get(*args, **kwargs):
        return HttpResponse('Pay')


class CloseOrder(View):
    def get(*args, **kwargs):
        return HttpResponse('CloseOrder')


class Details(View):
    def get(*args, **kwargs):
        return HttpResponse('Details')
