# Imports
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from api.serializers import UserSerializer

# BEGIN

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# END
