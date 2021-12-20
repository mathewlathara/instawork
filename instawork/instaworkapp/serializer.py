from rest_framework import serializers
from .models import Employee

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','first_name', 'last_name', 'email', 'phone_number', 'role_type')