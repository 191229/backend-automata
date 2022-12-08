from rest_framework import serializers
from lenguajes.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['conjunto']
            