from django import forms
from Appraisal.models import Appraisal


class EmpForm(forms.ModelForm):
    class Meta:
        model = Appraisal
        fields ="__all__"