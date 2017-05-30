from mapwidgets.widgets import GooglePointFieldWidget
from miot.models import PointOfInterest, Page
from django import forms

class PointOfInterestForm(forms.ModelForm):
    class Meta:
        model = PointOfInterest
        fields = ("name", "featured_image", "position", "tags", "active")
        widgets = {
            'position': GooglePointFieldWidget,
        }

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ("title", "content", "template")