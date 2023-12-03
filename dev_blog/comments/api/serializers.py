from rest_framework import serializers
from comments.models import Comment
from users.api.serializers import UserSerializer
from posts.api.serializers import PostSerializer


class CommentSerializer(serializers.ModelSerializer):
    post_data = serializers.SerializerMethodField()
    user_data = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'post', 'created_at', 'updated_at', 'post_data', 'user_data')

    def get_post_data(self, obj):
        post = obj.post
        return PostSerializer(post).data

    def get_user_data(self, obj):
        user = obj.user
        return UserSerializer(user).data
