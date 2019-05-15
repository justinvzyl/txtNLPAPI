from rest_framework import serializers
from .models import UserComment
from django.contrib.auth.models import User

class UserCommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = UserComment
        fields = ('url', 'created', 'topic', 'comment', 'polarity', 'subjectivity', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    usercomments = serializers.HyperlinkedRelatedField(many = True, view_name = 'usercomment-detail', read_only = True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'usercomments')