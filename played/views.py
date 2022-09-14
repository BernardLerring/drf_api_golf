from rest_framework import generics, permissions
from drf_api_golf.permissions import IsOwnerOrReadOnly
from played.models import Played
from played.serializers import PlayedSerializer


class PlayedList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PlayedSerializer
    queryset = Played.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlayedDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PlayedSerializer
    queryset = Played.objects.all()
