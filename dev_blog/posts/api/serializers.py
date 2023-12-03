from rest_framework import serializers
from posts.models import Post
from categories.api.serializers import CategorySerializer
from users.api.serializers import UserSerializer
 
 
class PostSerializer(serializers.ModelSerializer):
    category_data = serializers.SerializerMethodField()
    user_data = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image', 'user', 'category', 'created_at', 'updated_at', 'category_data', 'user_data')
 
    
    def get_category_data(self, obj):
      category = obj.category
      return CategorySerializer(category).data
 
    def get_user_data(self, obj):
        user = obj.user
        return UserSerializer(user).data