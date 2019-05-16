from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('usercomments/', views.UserCommentList.as_view(), name = 'usercomment-list'),
    path('usercomments/<int:pk>/', views.UserCommentDetail.as_view(), name = 'usercomment-detail'),
    path('users/', views.UserList.as_view(), name = 'user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name = 'user-detail'),
    path('uploadcsv/<filename>', views.BackLogCSVUpload.as_view()),
    path('backlog/', views.BackLogCommentList.as_view(), name='backlogcomment-list'),
    path('backlog/<int:pk>', views.BackLogCommentDetail.as_view(), name='backlogcomment-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)