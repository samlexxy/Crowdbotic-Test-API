from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import *


class AppSerializer(serializers.ModelSerializer):
    subscription = serializers.SerializerMethodField()
    class Meta:
        model = App
        fields = ['id', 'name', 'description', 'type', 'framework', 'domain_name', 'screenshot', 'subscription', 'user', 'created_at', 'updated_at']
        read_only_fields = ['id', 'screenshot', 'subscription', 'user', 'created_at', 'updated_at']

    def get_subscription(self, obj):
        # method = self.context['request'].method 
        # print(self.context['request'].method)
        
        # if method in ['PUT', 'POST', 'PATCH']:
        #     return ""
        # return obj.subscription.id

        try:
            return obj.subscription.id
        except Subscription.DoesNotExist:
            return ""

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'description', 'price', 'created_at', 'updated_at']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'plan', 'app', 'active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']