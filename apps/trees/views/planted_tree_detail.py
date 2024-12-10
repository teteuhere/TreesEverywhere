from rest_framework import generics
from ..models.planted_tree import PlantedTree
from ..services.planted_tree import PlantedTreeSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

class PlantedTreeDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlantedTreeSerializer
    def get_queryset(self):
        user = self.request.user
        return PlantedTree.objects.filter(planted_by__account=user.account)