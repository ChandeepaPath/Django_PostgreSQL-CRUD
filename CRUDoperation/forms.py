from django import forms
from  CRUDoperation.models import EmpDetails

class Empforms(forms.ModelForm):
    class Meta:
        model=EmpDetails
        fields="__all__"