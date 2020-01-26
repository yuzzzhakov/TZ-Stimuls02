from rest_framework import routers
from base import api_views

router = routers.DefaultRouter()
router.register(r'dogs', api_views.DogViewSet)
router.register(r'guardians', api_views.GuardianViewSet)
router.register(r'payments', api_views.PaymentViewSet)