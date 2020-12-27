from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='product_pictures/%Y/%m', blank=True,
                              null=True, height_field=None, width_field=None, max_length=None,)
    slug = models.SlugField(unique=True) 
    price_marketing = models.FloatField()
    price_marketing_promotion = models.FloatField(default=0)
    FIELDNAME = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples')
        )
    )

    def __str__(self):
        return self.name


class Variation(models.Model):
    product_variation = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField()
    price_promotion = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name or self.product_variation.name

