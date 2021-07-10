from django import forms

class dform(forms.ModelForm):
    class Meta:
        fields="__all__"