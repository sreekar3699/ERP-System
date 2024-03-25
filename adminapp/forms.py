from django import forms

from .models import Products


class DateInput(forms.DateInput):
    input_type = "date"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"    # it will display all the fields in the form except default fields like id and registrationtime
        widgets = {
            # "name":forms.TimeField(attrs={'class':'div2'})

        }    # additional features of the fields  #using this, we can change label name in the form
        #exclude = {"gender"}       #using this, we can hide the fields in the form
