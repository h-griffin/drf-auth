from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Fish
from .serializers import FishSerializer
from .permissions import ISAuthorOrReadOnly

class FishList(ListCreateAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

class FishDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (ISAuthorOrReadOnly)
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

