from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from .views import LedgerView

router = routers.DefaultRouter()
router.register('', LedgerView)


urlpatterns = [
    path('', include(router.urls)),    
    path('api-auth/', include('rest_framework.urls'))
]

