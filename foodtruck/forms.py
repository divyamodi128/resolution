from django import forms
from .models import Truck

class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'cols': 65, 'rows': 6}),
            'user': forms.HiddenInput()
        }
    
    def __init__(self, *args, **kwargs):
        super(TruckForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                # Assigns the Help Text as a PlaceHolder
                self.fields[field].widget.attrs.update({'placeholder':help_text})

    # name = forms.CharField(max_length=150)
    # website = forms.CharField(widget=forms.URLInput, max_length=250, required=False)
    # contact_no = forms.CharField(max_length=15, required=False)
    # emails = forms.CharField(widget=forms.EmailInput, max_length=100)
    # description = forms.CharField(widget=forms.Textarea(), required=True)
