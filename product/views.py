from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from .models import Product, Variation
from django.contrib import messages
from pprint import pprint


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
    def get(self, *args, **kwargs):
        http_refere = self.request.META.get(
            'HTTP_REFERER',
            reverse('product:list_product')
        )
        # TODO: id da variação selecionada do template
        variacao_id = self.request.GET.get('vid')

        # TODO: Retorna mensagem de erro caso não exista um produto selecionado
        if not variacao_id:
            messages.error(self.request, 'Produto não existe')
            return redirect(http_refere)

        # TODO: Selecionar expecificamente a variação que o cliente está querendo comprar
        variation = get_object_or_404(Variation, id=variacao_id)
        variation_stock = variation.stock
        #variation = Variation.objects.get(pk=variacao_id)

        product = get_object_or_404(Product, pk=variation.product_variation.id)

        product_id = product.id
        product_name = product.name
        variation_name = variation.name or ''
        variation_id = variation.id
        unique_price = variation.price
        price_promotion = variation.price_promotion
        amount = 1
        slug = product.slug
        image = product.image

        if image:
            image = image.name
        else:
            image = ''

        #print(f'--->{product_id} - {product_name}- {variation_name}')
        # messages.error(
        #    self.request, f'--->{product_id} - {product_name}- {variation_name}- {variation_name}')

        # TODO: Verifica se existe produto em estoque

        if variation.stock < 1:
            messages.error(
                self.request, f'Não existe produto em estoque - {variation.stock}')
            return redirect(http_refere)

        # TODO: Verifica se já existe a sessão caso contrario cria
        if not self.request.session.get('cart'):
            self.request.session['cart'] = {}
            self.request.session.save()

        cart = self.request.session['cart']

        # TODO: Verifica se a variação existe no cart
        if variacao_id in cart:
            amount_cart = cart[variacao_id]['amount']
            amount_cart += 1
            messages.error(
                self.request, f'Não existe produto em estoque - {amount_cart}')
            return redirect(http_refere)
        else:

            cart[variacao_id] = {
                'product_id': product_id,
                'product_name': product_name,
                'variation_name': variation_name,
                'variation_id': variation_id,
                'unique_price': unique_price,
                'price_promotion': price_promotion,
                'amount': 1,
                'slug': slug,
                'image': image,

            }
            self.request.session.save()

            messages.error(
                self.request, f'Produto não existe - {variation.name}')
            return redirect(http_refere)

        # TODO: verifica no atributo stock da variation se a valor maior que 1
        # caso contrário retorna uma mensagem de erro.
        if variation.stock < 1:
            messages.error(self.request, 'Estoque insuficiente')


class RemoveCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('RemoveCart')


class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Cart')


class Finish(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finish')
