from django import forms


class FileUploadForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'})
    )
    employee_id = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter unique ID'})
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter full address'})
    )
    file = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'accept': '.pdf'}),
        help_text='Upload PDF file (Max 10MB)'
    )
    photos = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'accept': 'image/jpeg,image/png', 'multiple': ''}),
        help_text='Upload photos (Max 5 files, JPG/PNG only, 5MB each)'
    )

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if file.size > 10 * 1024 * 1024:  # 10MB
                raise forms.ValidationError('File size must be less than 10MB')
            if not file.name.endswith('.pdf'):
                raise forms.ValidationError('Only PDF files are allowed')
        return file
