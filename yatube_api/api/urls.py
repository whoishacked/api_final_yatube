from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()
router.register('follow', FollowViewSet, basename="follow")
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register(r'posts/(?P<id>\d+)/comments', CommentViewSet,
                basename="comments")

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
