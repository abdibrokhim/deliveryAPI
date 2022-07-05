from django.contrib import admin
from . import models

# Register your models here.


class DeliverAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'auth_key',)
    list_filter = ('registered',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'size', 'amount', 'status', 'client', 'deliver',)
    list_filter = ('registered', 'status',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone_number',)
    list_filter = ('registered',)


admin.site.register(models.Deliver, DeliverAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Client, ClientAdmin)
