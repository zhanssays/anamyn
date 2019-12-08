from rest_framework import serializers
from ..models import Profile, PlanningChild
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'id']
        read_only_fields = ['username', 'id']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Profile
        fields = ['id', 'photo', 'date_of_birth', 'hide_age', 'city', 'marriage_status', 'user']
        depth = 1
        read_only_fields = ['id', 'user']

        #fields = ['first_name', 'last_name', 'email',]


class PlanningChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanningChild
        fields = '__all__'

