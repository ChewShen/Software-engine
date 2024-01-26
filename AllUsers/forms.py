from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control ', 'style': 'width: 300px;','autocomplete':'off'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','style': 'width: 300px;','autocomplete':'off'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','style': 'width: 300px;','autocomplete':'off'}))
    # role = forms.IntegerField(label='role')
     
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','password1','password2' )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        # user.arole = self.cleaned_data['role']  # Assign age to the user object

        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)


        # for field_name, field in self.fields.items():
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['style']='width: 300px;'
        self.fields['username'].widget.attrs['autocomplete'] = 'off'

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['style']='width: 300px;'
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['style']='width: 300px;'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    

class UserProfileChangeForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'rectangle-email rectangle-Remail','autocomplete': 'off'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'rectangle-username rectangle-Rusername', 'autocomplete': 'off'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'rectangle-fname rectangle-Rfname', 'autocomplete': 'off'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'rectangle-lname rectangle-Rlname', 'autocomplete': 'off'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'HouseUnit')

# class EmployeeProfileChangeForm(UserChangeForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'rectangle-email','autocomplete': 'off'}))
#     username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'rectangle-username', 'autocomplete': 'off'}))
#     first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'rectangle-fname', 'autocomplete': 'off'}))
#     last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'rectangle-lname', 'autocomplete': 'off'}))

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'first_name', 'last_name', 'email')


class PassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'frame-3', 'type':'password','placeholder':'old password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'frame-3', 'type':'password','placeholder':'new password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'frame-3', 'type':'password','placeholder':'confirm new password'}))
    

    class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')