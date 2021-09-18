from rest_framework.generics import ListCreateAPIView, ListAPIView

from .models import Contact, ProductImage
from .serializers import ContactSerializer, ProductImagesSerializer


class ContactListCreateView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ProductListView(ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImagesSerializer
