# Generated by Django 3.1.3 on 2020-11-24 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201124_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='type',
            field=models.CharField(choices=[('H', 'Home'), ('W', 'Work')], default='H', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
