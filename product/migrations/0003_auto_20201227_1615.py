# Generated by Django 3.1.4 on 2020-12-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='FIELDNAME',
            field=models.CharField(choices=[('V', 'Variável'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]
