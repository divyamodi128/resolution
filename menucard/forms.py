from django import forms
from .models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'cols': 65, 'rows': 6}),
            'user': forms.HiddenInput(),
            'truck': forms.HiddenInput()
        }
    
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ('is_dish',):
                self.fields[field].widget.attrs.update({'class':'form-control'})
        