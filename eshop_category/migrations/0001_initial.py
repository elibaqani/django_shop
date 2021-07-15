# Generated by Django 3.1.1 on 2020-10-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoroductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='عنوان')),
                ('name', models.CharField(max_length=21, verbose_name='عنوان در url')),
            ],
            options={
                'verbose_name': 'دسته بندی محصول',
                'verbose_name_plural': 'دسته بندی محصولات',
            },
        ),
    ]
