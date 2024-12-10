from django.contrib import admin
from ..models import Account, User, Profile

# Define a action para ativar/desativar contas
def enable_disable_accounts(modeladmin, request, queryset):
    for account in queryset:
        account.is_active = not account.is_active
        account.save()

# Define o texto que será exibido na interface do admin
enable_disable_accounts.short_description = "Ativar/Desativar contas"

# Registra os modelos no admin
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')  # Exibe o status 'is_active'
    actions = [enable_disable_accounts]  # Registra a action

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'account', 'is_active')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'about')