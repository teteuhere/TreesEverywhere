from django.contrib.auth.forms import UserCreationForm
from ..models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'account') 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicione classes CSS para estilização
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})