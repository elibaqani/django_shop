# Generated by Django 3.1.1 on 2020-11-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product', '0005_productgallery_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visit_count',
            field=models.IntegerField(default=0),
        ),
    ]
