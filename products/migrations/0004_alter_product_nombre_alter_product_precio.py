# Generated by Django 4.2.1 on 2023-06-04 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_marca_categoria_sigla_alter_product_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='precio',
            field=models.DecimalField(decimal_places=0, max_digits=9),
        ),
    ]
