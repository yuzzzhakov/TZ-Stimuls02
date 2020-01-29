from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet
from .models import Dog, Guardian, Payment
from .serializers import *
from rest_framework.response import Response
from rest_framework import status



class DogsListView(ListView):
    model = Dog
    template_name = 'base/base.html'
    context_object_name = 'dogs'


class DogViewApi(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if instance.fixed:
            serializer.is_valid(raise_exception=True)
            if request.data.get('fixed'):
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                self.perform_update(serializer)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.fixed:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)


class GuardianViewApi(ModelViewSet):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer

    def fixed_status(self):
        instance = self.get_object()
        fixed_status = False
        for dog in instance.dog_set.all():
            if dog.fixed:
                fixed_status = True
                break
        return fixed_status

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if self.fixed_status():
            serializer.is_valid(raise_exception=True)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.fixed_status:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentViewApi(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def fixed_status(self):
        instance = self.get_object()
        fixed_status = False
        for dog in instance.purpose.all():
            if dog.fixed:
                fixed_status = True
                break
        return fixed_status

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if self.fixed_status():
            serializer.is_valid(raise_exception=True)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.fixed_status:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)