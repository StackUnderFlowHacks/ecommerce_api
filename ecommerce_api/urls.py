from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from API import views


router = routers.DefaultRouter()
router.register(r'user', views.DetailsView, 'user')
router.register(r'address', views.AddressView, 'address')


urlpatterns = [
    path('', include('API.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
