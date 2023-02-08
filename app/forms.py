from django import forms
from app.models import *
class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class ModelWebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'

class ModelAccess_RecordForm(forms.ModelForm):
    class Meta:
        model=Access_Record
        fields='__all__'
            