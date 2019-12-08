from ..models import Profile, PlanningChild
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import ProfileSerializer, PlanningChildSerializer, UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PlanningChildViewSet(viewsets.ModelViewSet):
    queryset = PlanningChild.objects.all()
    serializer_class = PlanningChildSerializer
