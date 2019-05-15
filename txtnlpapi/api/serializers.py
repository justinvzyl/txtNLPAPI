from rest_framework import serializers
from .models import UserComment
from django.contrib.auth.models import User
from .nlp_utils import SentimentAnalyzer

class UserCommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = UserComment
        fields = ('url', 'created', 'topic', 'comment', 'polarity', 'subjectivity', 'owner')
        read_only_fields = ('polarity', 'subjectivity', 'owner', 'created')
    
    def create(self, validated_data):
        sentiments = SentimentAnalyzer(validated_data['comment']).get_sentiment()
        validated_data.update(sentiments)
        return UserComment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        sentiment = SentimentAnalyzer(validated_data.get('comment')).get_sentiment()
        instance.polarity = sentiment['polarity']
        instance.subjectivity = sentiment['subjectivity']
        instance.comment = validated_data.get('comment')
        instance.topic = validated_data.get('topic')
        instance.save()
        return instance

class UserSerializer(serializers.HyperlinkedModelSerializer):
    usercomments = serializers.HyperlinkedRelatedField(many = True, view_name = 'usercomment-detail', read_only = True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'usercomments')