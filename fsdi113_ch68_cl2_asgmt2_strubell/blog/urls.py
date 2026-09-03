from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostDraftListView,
    PostArchivedListView,
    ProtectedPostDetailView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/protected/<int:pk>/', ProtectedPostDetailView.as_view(), name='post_detail_protected'),
    path('drafts/', PostDraftListView.as_view(), name='post_draft_list'),
    path('archived/', PostArchivedListView.as_view(), name='post_archived_list'),
]
