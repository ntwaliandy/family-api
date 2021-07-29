
from rest_framework import serializers
from .models import Family

class FamilySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Family
        fields = ('first_name', 'second_name', 'age', 'gender', 'phone_number', 'phone_type')