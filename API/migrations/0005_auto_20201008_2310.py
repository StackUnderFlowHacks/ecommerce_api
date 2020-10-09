# Generated by Django 3.1.2 on 2020-10-08 17:40

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20201008_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=False, help_text='is product available for purchases?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(default='', help_text='Name of manufacturer', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Name of product', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='payment_option',
            field=models.CharField(default='Cash On Delivery (C.O.D.)', help_text="What's the payment options available on product", max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveBigIntegerField(default=0, help_text='Available quantity of product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail_link',
            field=models.CharField(blank=True, default='', help_text='Paste link of thumbnail photo', max_length=100),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=None, max_length=20), blank=True, default=None, help_text='Define category of product', size=None),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='country_of_origin',
            field=models.CharField(default=None, help_text="What's the Country of Origin", max_length=20),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='coupons',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=None, max_length=20), blank=True, default=None, help_text='coupon codes for this product separated by commas', size=None),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='how much discount is ongoing for product (in %)', max_digits=12),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='photos_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=None, max_length=450), blank=True, default=None, help_text='Paste links for the photos of products separated by commas', size=None),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='product_id',
            field=models.OneToOneField(help_text='Select product ID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='API.product'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='rating out of 5', max_digits=5),
        ),
    ]
