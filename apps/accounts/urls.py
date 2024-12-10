from django.urls import path
from.views.account_list import AccountList
from.views.account_detail import AccountDetail
from apps.accounts.views.register import register_view
from apps.accounts.views.account_trees import account_trees
from apps.accounts.views.disable_enable import enable_disable_accounts

urlpatterns = [
    path('accounts/', AccountList.as_view()),
    path('accounts/<int:pk>/', AccountDetail.as_view()),
    path('register/', register_view, name='register'),
    path('planted/', account_trees, name='account_trees'),
    path('eadmin_accounts/', enable_disable_accounts, name='admin_account'),
]