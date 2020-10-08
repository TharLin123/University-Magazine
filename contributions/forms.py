from django import forms
from .models import Contribution

class ContributionForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={"id" :"file-input",'multiple': True,"(change)":"handleFileInput($event.target.files)"}))

    class Meta:
        model = Contribution
        fields = ('word_docu','author','images','faculty')

        widgets = {
            'author' : forms.HiddenInput(),
            'faculty' : forms.HiddenInput(),
            'title' : forms.TextInput(attrs={"class" : "form-control", "id" : "setting-input-1", 'autofocus':True}),
        }

class EditContributionForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={"id" :"file-input"}),required=False)
    images2 = forms.FileField(widget=forms.ClearableFileInput(attrs={"id" :"file-input"}),required=False)
    images3 = forms.FileField(widget=forms.ClearableFileInput(attrs={"id" :"file-input"}),required=False)

    class Meta:
        model = Contribution
        fields = ('title','author','images','images2','images3','paragraphs','faculty')

        widgets = {
            'author' : forms.HiddenInput(),
            'faculty' : forms.HiddenInput(),
            'paragraphs' : forms.Textarea(attrs={"class" : "form-control", "id" : "exampleFormControlTextarea5", 'style':'height:300px;'}),
            'title' : forms.TextInput(attrs={"class" : "form-control", "id" : "setting-input-1", 'autofocus':True}),
        }