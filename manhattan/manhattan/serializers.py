from rest_framework import serializers
from . import models


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'street_address',
            'city',
            'state',
            'phone_number',
            'owner_name',
            'owner_email',
            'business_type'
        )
        model = models.Business
