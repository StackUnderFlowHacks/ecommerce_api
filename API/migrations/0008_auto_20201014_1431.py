# Generated by Django 3.1.2 on 2020-10-14 14:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_address_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='addressId',
            field=models.UUIDField(default=uuid.UUID('aade6375-310d-45eb-a181-0baad1e883c6'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='details',
            name='userId',
            field=models.UUIDField(default=uuid.UUID('cfd7856f-5ba4-40bf-950a-1840109585d4'), editable=False, primary_key=True, serialize=False),
        ),
    ]
