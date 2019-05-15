from .models import UserComment
from .serializers import UserCommentSerializer
from rest_framework import generics

class UserCommentList(generics.CreateAPIView):
    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer

class UserCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer