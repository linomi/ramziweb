from django import forms
class PromptForm(forms.Form):
    scholar_query = forms.CharField(
        label="Search on Google scholar",
        max_length=100,
        error_messages={'required':"This fill cant be empty","max_length":"Your query is too long "})
