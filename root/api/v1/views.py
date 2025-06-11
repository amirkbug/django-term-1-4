from rest_framework.viewsets import ModelViewSet
from .serializer import ContactUsSerializer

class ContactView(ModelViewSet):
    serializer_class = ContactUsSerializer