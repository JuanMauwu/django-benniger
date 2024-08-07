from rest_framework import generics, viewsets

# Create your views here.
from rest_framework.response import Response
from myapp.models import DetailReview
from myapp.serializers import DetailReviewSerializer

class DetailReviewViewSet(viewsets.ModelViewSet):
    queryset = DetailReview.objects.all()
    serializer_class = DetailReviewSerializer


"""
class DetailReviewListAPIView(generics.ListAPIView):
    queryset = DetailReview.objects.filter(active=True)
    serializer_class = DetailReviewSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"values": serializer.data})
"""