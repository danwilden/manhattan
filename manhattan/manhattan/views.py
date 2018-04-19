from rest_framework import generics

from . import models
from . import serializers


class ListBusiness(generics.ListCreateAPIView):
    queryset = models.Business.objects.all()
    serializer_class = serializers.BusinessSerializer


class DetailBusiness(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Business.objects.all()
    serializer_class = serializers.BusinessSerializer
