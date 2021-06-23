from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Glass
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer
# Create your views here.


class PostsList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Glass.objects.all()
    serializer_class = PostSerializer

class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Glass.objects.all()
    serializer_class = PostSerializer
    