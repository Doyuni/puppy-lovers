from django.urls import path
from .views import review, PostListView, PostDetailView, PostCreateView, ReviewCreateView, ReviewDetailView, review_comment_create, ReviewListView


urlpatterns = [
    path('board', PostListView.as_view(), name='board'),
    path('board/<int:pk>', PostDetailView.as_view(), name='board_detail'),
    path('board/new', PostCreateView.as_view(), name='board_create'),
    path('review', ReviewListView.as_view(), name='review'),
    path('review/new', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>', ReviewDetailView.as_view(), name='review_detail'),
    path('review/<int:pk>/comments', review_comment_create, name='review_comment_create'),
#    path('post/<int:pk>/comments', post_comment_create, name='post_comment_create'),
]
