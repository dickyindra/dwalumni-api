from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Company

class CompanySerialize(serializers.ModelSerializer):
    created_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
    updated_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'address',
            'user',

            # general fields
            'is_active',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )
