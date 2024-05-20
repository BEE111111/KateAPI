from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password, check_password


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        try:
            user = User.objects.get(username=username)
            if user and check_password(password, user.password):
                data['user'] = user
            else:
                raise serializers.ValidationError("Incorrect username or password.")
        except User.DoesNotExist:
            raise serializers.ValidationError("Incorrect username or password.")
        return data
