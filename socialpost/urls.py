from django.urls import path

from .views import (
    SocialPostListView,
    SocialPostDetailView,
    SocialPostDeleteView,
    SocialPostUpdateView,
    SocialPostCreateView,
)

urlpatterns = [
    path('', SocialPostListView.as_view(), name='socialpost_list'),
    path('<int:pk>/edit/', SocialPostUpdateView.as_view(), name='socialpost_edit'),
    path('<int:pk>/detail/', SocialPostDetailView.as_view(), name='socialpost_detail'),
    path('<int:pk>/delete/', SocialPostDeleteView.as_view(), name='socialpost_delete'),
    path('new/', SocialPostCreateView.as_view(), name='socialpost_create')
]