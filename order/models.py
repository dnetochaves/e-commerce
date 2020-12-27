from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default="C",
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )
    def __str__(self):
        return f'Pedido N. {self.pk}'
    

class ItemOrder(models.Model):
    order_item = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    variaction_name = models.CharField(max_length=255)
    variaction_id = models.PositiveIntegerField()
    price = models.FloatField()
    price_promotion = models.FloatField()
    amount = models.PositiveIntegerField()
    image = models.CharField(max_length=2000)

    def __str__(self):
        return f'Item do {self.order_item}'
    