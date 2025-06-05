from django import forms
from django.forms.widgets import ClearableFileInput
from django.core.validators import FileExtensionValidator

class PromptForm(forms.Form):
    scholar_query = forms.CharField(required=True,
        label="Search on Google scholar",
        max_length=100,
        error_messages={'required': "This field can't be empty", 'max_length': "Your query is too long "})
    
    CV = forms.FileField(
        allow_empty_file=False,
        required=False,
        validators=[FileExtensionValidator(
            allowed_extensions=['pdf'],
            message="Only PDF files are allowed!"
        )],
        widget=ClearableFileInput(
            attrs={'accept': '.pdf'}  # This adds client-side file type filtering
        )
    )

    def clean_CV(self):
        cv_file = self.cleaned_data.get('CV')
        if cv_file:
            if not cv_file.name.lower().endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed!")
            # Optional: You can also check file size here
            if cv_file.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("File size must be under 5MB!")
        return cv_file