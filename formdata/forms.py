from django import forms
from wagtail.images.models import Image
from wagtail.images.widgets import AdminImageChooser


class ImageForm(forms.Form):
    image = forms.ModelChoiceField(
        queryset=Image.objects.all(), widget=AdminImageChooser
    )
    alignment = forms.ChoiceField(choices=[
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right'),
    ], widget=forms.RadioSelect)
    caption = forms.CharField()
    credit = forms.CharField()
