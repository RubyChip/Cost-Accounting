from django.shortcuts import render
from rest_framework import viewsets

from .models import Ledger
from .serializers import LedgerSerializer
class LedgerView(viewsets.ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer