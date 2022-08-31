from .models import Menu
from .serializers import MenuSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerOrReadOnly

class MenuList(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer