from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializer import *
from .models import *


class AppViewSet(viewsets.ModelViewSet):
    # queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return App.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # # def update(self, request, *args, **kwargs):
    # #     super(AppViewSet, self).update(request, *args, **kwargs)
    # #     return Response({"message": "Success"})
    
    # def create(self, request, *args, **kwargs):
    #     super(AppViewSet, self).create(request, *args, **kwargs)
    #     return Response({"status": "Success"})



class PlanViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,]
    def list(self, request):
        qs = Plan.objects.all()
        serializer = PlanSerializer(qs, many=True)
        return Response(serializer.data) 

    def retrieve(self, request, pk=None):
        qs = Plan.objects.all()
        plan = get_object_or_404(qs, pk=pk)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)

class SubscriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    # queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)
    
# Create your views here.


