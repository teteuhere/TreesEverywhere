from rest_framework import generics
from ..models.account import Account
from ..services.account_serializer import AccountSerializer

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer