from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('usercomments/', views.UserCommentList.as_view(), name = 'usercomment-list'),
    path('usercomments/<int:pk>/', views.UserCommentDetail.as_view(), name = 'usercomment-detail'),
    path('users/', views.UserList.as_view(), name = 'user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name = 'user-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)