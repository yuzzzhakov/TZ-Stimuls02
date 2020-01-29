from rest_framework import serializers
from .models import Dog, Guardian, Payment


class DogSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField('get_full_name')

    def get_full_name(self, dog):
        return dog.name + ' ' + dog.breed

    class Meta:
        model = Dog
        fields = '__all__'


class GuardianSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField('get_full_name')

    def get_full_name(self, guardian):
        return guardian.name + ' ' + guardian.surname

    class Meta:
        model = Guardian
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
