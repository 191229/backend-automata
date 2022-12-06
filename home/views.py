
from rest_framework.viewsets import ModelViewSet
from home.serializers import PostSerializer
import json
from home.models import Post

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()