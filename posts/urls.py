from django.urls import path
from .views import(PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostArchivedListView, PostDraftListView)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),    # Here, we are accessing the function by calling the class method as_view().
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),  # This path is a special one.
    path("new/", PostCreateView.as_view(), name="post_new"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="post_edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
    path("archived/", PostArchivedListView.as_view(), name="post_archived"),
    path("drafts/", PostDraftListView.as_view(), name="post_drafts"),
]
