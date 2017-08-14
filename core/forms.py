from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import Profile


class ProfileForm(forms.ModelForm):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    CHOICES = (
        ('USER', 'User'),
        ('DRIVER', 'Driver'),
    )
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    gender =     forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect)
    bio =        forms.CharField(max_length=500, required=False, 
                                 widget=forms.Textarea(attrs={'cols': 65, 'rows': 6}), 
                                 help_text='Short Descriptions about yourself')
    location =   forms.CharField(max_length=30, required=False, help_text='Your Locations')
    image =      forms.ImageField()
    attribute =  forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Profile
        fields = ('birth_date', 'gender', 'bio', 'location', 'image', 'attribute')
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ('gender', 'attribute',):
                self.fields[field].widget.attrs.update({'class':'form-control'})

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name =  forms.CharField(max_length=30, required=False, help_text='Optional.')
    email =      forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # import pdb ; pdb.set_trace()
        for field in self.fields:
            if field not in ('gender', 'attribute',):
                self.fields[field].widget.attrs.update({'class':'form-control'})
            # help_text = self.fields[field].help_text
            # self.fields[field].help_text = None
            # if help_text != '':
            #     # Assigns the Help Text as a PlaceHolder
