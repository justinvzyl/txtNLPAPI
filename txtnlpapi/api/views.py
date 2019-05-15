from .models import UserComment
from .serializers import UserCommentSerializer, UserSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import status

@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'usercomments': reverse('usercomment-list', request = request, format = format),
        'users': reverse('user-list', request = request, format = format)
    })

class UserCommentList(generics.ListCreateAPIView):
    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    
class UserCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly,)

# class UserCommentCSVUpload(APIView):
#     parser_classes = (FileUploadParser,)

#     def put(self, request, filename, format = None):
#         if 'file' not in request.data:
#             raise ParseError('Empty content.')

#         file_obj = request.data['file'].read()
        
#         print(type(file_obj))
#         return Response(status=204)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
