from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class Create(View):
     def get(*args, **kwargs):
        return HttpResponse('Create')

class Update(View):
    def get(*args, **kwargs):
        return HttpResponse('Update')

class Login(View):
    def get(*args, **kwargs):
        return HttpResponse('Login')

class Logout(View):
    def get(*args, **kwargs):
        return HttpResponse('Logout')
