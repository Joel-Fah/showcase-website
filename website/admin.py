from django.contrib import admin
from .models import ContactInfo, Subscriber

# Register your models here.
admin.site.register(ContactInfo)
admin.site.register(Subscriber)