from rest_framework import serializers
from .models import Scientist



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scientist
        fields = ['username', 'author_in_russian', 'first_author',
                  'job_title', 'relations', 'science_title']

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)


class ScientistDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scientist
        fields = ['username', 'author_in_russian', 'first_author',
                  'job_title', 'relations', 'science_title']



class ScientistUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scientist
        fields = ['username', 'author_in_russian', 'first_author',
                  'job_title', 'relations', 'science_title']

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance