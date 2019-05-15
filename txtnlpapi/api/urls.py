from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('usercomments/', views.UserCommentList.as_view(), name = 'usercomment-list'),
    path('usercomments/<int:pk>/', views.UserCommentDetail.as_view(), name = 'usercomment-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)