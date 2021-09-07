from django.forms import ModelForm
from demo.models.region import region



class regionForm(ModelForm) :
    class Meta:
        model =	region
        fields = ("name",)