from django.contrib import admin
from .models import Dog, Guardian, Payment

admin.site.register(Dog)
admin.site.register(Guardian)
admin.site.register(Payment)
