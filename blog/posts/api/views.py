from rest_framework.viewsets import ModelViewSet
from posts.models import Posts
from posts.api.serializers import PostsSerializer
from posts.api.permissions import IsAdminOrReadOnly

class PostsApiViewSet(ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]
    serializer_class=PostsSerializer
    queryset=Posts.objects.filter(published=True)
