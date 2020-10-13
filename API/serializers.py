from rest_framework import serializers
from .models import *


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ('userId', 'name', 'email', 'password', 'phone')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('userId', 'addressId', 'type', 'area', 'city', 'pinCode', 'state', 'country')
