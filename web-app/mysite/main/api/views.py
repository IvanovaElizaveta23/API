from rest_framework import generics
from ..models import Product
from .serializers import SubjectSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = SubjectSerializer