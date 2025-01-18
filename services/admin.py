from django.contrib import admin
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    #readonly_fields = ('status',) if you want your field to be read-only
    list_display = ('email', 'customer_name', 'status', 'created_at', 'updated_at') 
    list_filter = ('status',)

admin.site.register(ServiceRequest, ServiceRequestAdmin)
