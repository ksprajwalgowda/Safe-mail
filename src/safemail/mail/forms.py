from django import forms  

from . import models

class Composeform(forms.ModelForm):  
    class Meta:  
        model = models.Mailbox  
        fields = "__all__"  