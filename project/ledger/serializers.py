from rest_framework import serializers

from .models import Ledger


class LedgerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ledger
        fields = ['category_id', 'amount', 'description', 'created']


       