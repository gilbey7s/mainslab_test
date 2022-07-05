from rest_framework import serializers
from django.db.models import Sum

from .models import *


class ClientSerializer(serializers.ModelSerializer):
    amount_org = serializers.SerializerMethodField()
    profit = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ("name", "amount_org", "profit")

    def get_amount_org(self, obj):
        count_org = ClientOrganization.objects.filter(client_name=obj).count()
        return count_org

    def get_profit(self, obj):
        result = Bill.objects.filter(client_name=obj).aggregate(sum = Sum('sum'))
        return result['sum']


class BillSerializers(serializers.ModelSerializer):
    client_name = serializers.StringRelatedField(read_only=True)
    client_org = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Bill
        fields = ("__all__")