from django.contrib import admin
from .models import *

# Register your models here.


class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type', 'domain_name', 'framework', 'user')

class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at')

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('plan', 'app', 'user', 'active')


admin.site.register(App, AppAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Plan, PlanAdmin)
