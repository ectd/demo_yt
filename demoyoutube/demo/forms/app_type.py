from django.forms import ModelForm
from demo.models.app_type import app_type



class app_typeForm(ModelForm) :
    class Meta:
        model =	app_type
        fields = ("name",)