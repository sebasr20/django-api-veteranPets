# Generated by Django 4.2.1 on 2023-06-04 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_nombre_alter_product_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
    ]