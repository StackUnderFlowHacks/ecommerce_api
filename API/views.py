from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import *
from .models import *


def home(request):
    prod = Product.objects.all()
    print("\nresult:\n")
    out = ""
    for p in prod:
        out += f" ({p}) "
        print(f"{p}\n")
    return HttpResponse(f'''
    <h1>Home Page</h1><br>
    Total products are {out}
    ''')


class DetailsView(viewsets.ModelViewSet):
    serializer_class = DetailsSerializer
    queryset = Details.objects.all()


class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
