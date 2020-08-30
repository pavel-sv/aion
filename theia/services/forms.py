from django import forms

FILE_CHOISE = [
    ('CO', 'Customer Order lines'),
    ('PO', 'Purcase Order lines')
]


class UploadForm(forms.Form):
    upload = forms.FileField(allow_empty_file=False)


class FileClassForm(forms.Form):
    option = forms.CharField(widget=forms.Select(choices=FILE_CHOISE))
