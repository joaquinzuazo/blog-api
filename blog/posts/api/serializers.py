from rest_framework import serializers
from posts.models import Posts
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer

class PostsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category=CategorySerializer()
    class Meta:
        model=Posts
        fields=['title','content','slug','miniature','created_at','published','user','category']