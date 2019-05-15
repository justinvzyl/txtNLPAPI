from .models import UserComment
from .serializers import UserCommentSerializer, UserSerializer
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.contrib.auth.models import User

@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'usercomments': reverse('usercomment-list', request = request, format = format),
        'users': reverse('user-list', request = request, format = format)
    })

class UserCommentList(generics.ListCreateAPIView):
    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class UserCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
