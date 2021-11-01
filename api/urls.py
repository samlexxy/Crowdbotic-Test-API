from django.contrib import admin
from django.db.models import base
from rest_framework import routers, urlpatterns
from .views import PlanViewSet, AppViewSet, SubscriptionViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'apps', AppViewSet, basename='app')
router.register(r'plans', PlanViewSet, basename='plan')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')
urlpatterns = router.urls

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
