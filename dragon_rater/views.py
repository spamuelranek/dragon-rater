from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Dragon
from .serializer import DragonSerializer

class DragonAPIListView(ListCreateAPIView):
  queryset = Dragon.objects.all()
  serializer_class = DragonSerializer

class DragonAPIDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Dragon.objects.all()
  serializer_class = DragonSerializer