from django.forms import ModelForm
from .models import GuardianInfo


class GuardianForm(ModelForm):
    class Meta:
        model = GuardianInfo
        fields = '__all__'
