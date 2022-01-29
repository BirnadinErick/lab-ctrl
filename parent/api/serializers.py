# Imports
from django.contrib.auth.models import User
from rest_framework import serializers

# BEGIN

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

# END

if __name__ == '__main__':
    pass