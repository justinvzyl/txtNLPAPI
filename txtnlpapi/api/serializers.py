from rest_framework import serializers
from .models import UserComment

class UserCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserComment
        fields = ('url', 'created', 'topic', 'comment', 'polarity', 'subjectivity')