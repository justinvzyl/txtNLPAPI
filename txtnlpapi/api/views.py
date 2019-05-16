from .models import UserComment, BackLogComment
from .serializers import UserCommentSerializer, UserSerializer, BackLogSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.exceptions import ParseError
from rest_framework.parsers import MultiPartParser
from .parsers import PlainTextParser
from rest_framework.views import APIView
from rest_framework import status
from .tasks import csv_to_usercomment
import pandas as pd

@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'usercomments': reverse('usercomment-list', request = request, format = format),
        'users': reverse('user-list', request = request, format = format),
        'backlog': reverse('backlogcomment-list', request= request, format = format)
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

class BackLogCSVUpload(APIView):
    parser_classes = (MultiPartParser,)

    def put(self, request, filename, format = None):
        csv_df = pd.read_csv(request.data[filename])
        csv_json = csv_df.to_json(orient='index')
        print(csv_json)
        csv_to_usercomment.delay(csv_json)

        return Response(status=204)

class BackLogCommentList(generics.ListAPIView):
    queryset = BackLogComment.objects.all()
    serializer_class = BackLogSerializer

class BackLogCommentDetail(generics.RetrieveAPIView):
    queryset = BackLogComment.objects.all()
    serializer_class = BackLogSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
