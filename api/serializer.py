import re
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_name(self, value):
        print("value name",value)
        if not re.match(r'^[A-Za-z ]*$', value):
            raise serializers.ValidationError("Name should not contain Special Characterssssss")
        return value

    def validate_age(self, value):
        print("value age",value)
        if value < 18:
            raise serializers.ValidationError("Age should be greater than 18")
        return value 

