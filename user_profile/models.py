from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
import re
from utils.validacpf import valida_cpf


class UserProfile(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    birth_date = models.DateField()
    cpf = models.CharField(max_length=11)
    adress = models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    complement = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=8)
    city = models.CharField(max_length=30)
    FIELDNAME = models.CharField(
        max_length=2,
        default='BA',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )
    def __str__(self):
        return f'{self.user_profile.first_name}'
    
    def clean(self):
        error_message = {}

        if not valida_cpf(self.cpf):
            error_message ['cpf'] = 'Digite um cpf válido'
        
        if re.search(r'[^0-9]', self.zip_code) or len(self.zip_code) < 8:
            error_message['zip_code'] = 'CEP inválido, digite apenas numeros.'

        if error_message:
            raise ValidationError(error_message)
        

    
