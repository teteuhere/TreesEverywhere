from rest_framework import generics
from ..models.account import Account
from ..services import AccountSerializer

class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
