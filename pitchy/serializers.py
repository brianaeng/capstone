from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import Profile, Friendship, Focus, User, Conversation, DirectMessage

# Serializers define the API representation.
# This is which attributes the API outputs

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email',)
