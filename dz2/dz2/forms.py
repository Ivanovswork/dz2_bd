from django.forms import ModelForm
from .models import Clients


class ClientForm(ModelForm):
    class Meta:
        model = Clients
        exclude = ()