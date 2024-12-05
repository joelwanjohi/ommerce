# Generated by Django 4.2.6 on 2023-11-07 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Vegetables', 'Vegetables'), ('Fruits', 'Fruits'), ('Meat, Poultry & Dairy', 'Meat, Poultry & Dairy'), ('Farm Feeds', 'Farm Feeds')], default='Vegetables', max_length=25),
        ),
    ]
