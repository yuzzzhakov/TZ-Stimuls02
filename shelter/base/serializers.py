from rest_framework.serializers import ModelSerializer
from .models import *


class DogSerializer(ModelSerializer):
    class Meta:
        model = Dog
        fields = ['name', 'date_of_birth', 'breed', 'guardian']


class GuardianSerializer(ModelSerializer):
    class Meta:
        model = Guardian
        fields = ['name', 'surname', 'email', 'phone']


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ['sum', 'currency', 'purpose']

