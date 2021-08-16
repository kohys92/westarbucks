# Generated by Django 3.2.6 on 2021-08-15 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='nutrition',
        ),
        migrations.AddField(
            model_name='allergy',
            name='product',
            field=models.ManyToManyField(to='products.Product'),
        ),
        migrations.DeleteModel(
            name='Nutritions',
        ),
    ]
