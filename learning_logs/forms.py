from django import forms
from .models import Topic,Entry
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        #inheritance,and field labels is what attribute to inherit 
        model = Entry
        fields= ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs ={'cols':80})}