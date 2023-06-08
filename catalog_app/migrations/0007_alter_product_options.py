# Generated by Django 4.2.1 on 2023-06-08 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0006_alter_product_options_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'permissions': [('set_published_product', 'Can publish product'), ('change_description_product', 'Can change product description'), ('change_product_category', 'Can change product category')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
