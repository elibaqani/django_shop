# Generated by Django 3.1.1 on 2020-10-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_category', '0001_initial'),
        ('eshop_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='eshop_category.PoroductCategory'),
        ),
    ]