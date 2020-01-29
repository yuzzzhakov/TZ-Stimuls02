from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import *


router = SimpleRouter()
router.register('api/dogs', DogViewApi)
router.register('api/guardians', GuardianViewApi)
router.register('api/payments', PaymentViewApi)

urlpatterns = [
    path('', DogsListView.as_view(), name='dogs-list')
]

urlpatterns += router.urls
