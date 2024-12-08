from django.urls import path
from.views.account_list import AccountList
from.views.account_detail import AccountDetail

urlpatterns = [
    path('accounts/', AccountList.as_view()),
    path('accounts/<int:pk>/', AccountDetail.as_view()),

]