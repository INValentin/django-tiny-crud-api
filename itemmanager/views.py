from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from itemmanager.serializers import ItemSerializer
from itemmanager.models import Item

# Create your views here.



class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]