from rest_framework import viewsets # type: ignore

# Create your views here.
from rest_framework.response import Response # type: ignore
from myapp.models import Tag
from myapp.serializers import TagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

"""
class TagListAPIView(generics.ListAPIView):
    #queryset = Tag.objects.filter(active=True)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"values": serializer.data})
"""