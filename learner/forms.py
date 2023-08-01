from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User
from . models import Assesment, Document, School, Student,Score, StrandCreate, Profile, Gallery,Teacher,Message, Myclub, AddtoClub, ClubActivity,Contact
from django.forms import ModelForm, HiddenInput

from learner import models


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password' ,'class': 'form-control'}))



class CustomerRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    email= forms.CharField(widget=forms.EmailInput(attrs={'autofocus': 'True', 'class':'form-control'}))
    password1=forms.CharField(label= 'Password' ,widget=forms.PasswordInput(attrs={ 'class': 'form-control'}))
    password2=forms.CharField(label= 'Confirm Password' ,widget=forms.PasswordInput(attrs={ 'class': 'form-control'}))

    class Meta:
        model =User
        fields= ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(CustomerRegistrationForm, self).__init__(*args, **kwargs)
        

        
    
class MyPasswordChangeForm(PasswordChangeForm):
    old_password= forms.CharField(label='old Password',widget= forms.PasswordInput(attrs={'autofocus': 'True','autocomplete':'current-password','class': 'form-control'}))
    new_password1= forms.CharField(label='New Password',widget= forms.PasswordInput(attrs={'autocomplete':'current-password','class': 'form-control'}))
    new_password2= forms.CharField(label='Confirm New Password',widget= forms.PasswordInput(attrs={'autocomplete':'current-password','class': 'form-control'}))



class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))



class MySetPasswordForm(SetPasswordForm):
    new_password1= forms.CharField(label='New Password',widget= forms.PasswordInput(attrs={'autocomplete':'current-password','class': 'form-control'}))
    new_password2= forms.CharField(label='Confirm New Password',widget= forms.PasswordInput(attrs={'autocomplete':'current-password','class': 'form-control'}))

class AssesmentForm(ModelForm):
    class Meta:
        model =Assesment
        fields= '__all__'
        exclude= ( 'date_created',)

    def __init__(self, *args, **kwargs):
        super(AssesmentForm, self).__init__(*args, **kwargs)
    
        # self.fields['strand'].queryset = StrandCreate.objects.filter(grade=self.fields['grade'])
        var = self.fields['student']
        var.disabled = True
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control'})
            self.fields['student'].widget = forms.HiddenInput()


        

        # self.fields['student'].help_text ='You can search student details  '
        # self.fields['strand'].help_text ='select the strand you have tought  '
        # self.fields['expectation'].help_text='Award the Expectation on how the child understood |  KEY: EX- Exceeding expextation, MT-Meet Expectation, AP- Approaches epectation, BE- below expectation' 






class StudentForm(ModelForm):
    class Meta:
        model= Student
        fields= '__all__'
        exclude= ( 'date_created',)
    
    def __init__(self, *args, **kwargs):
        super(StudentForm, self). __init__( *args, **kwargs)
        var = self.fields['school']
        var.disabled = True
        
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control'})
            self.fields['school'].widget = forms.HiddenInput()

            
    

class ScoreForm(ModelForm):
    class Meta:
        model= Score
        fields= '__all__'
        exclude= ( 'date_created',)
    
    def __init__(self, *args, **kwargs):
        super(ScoreForm, self). __init__( *args, **kwargs)
        var = self.fields['student']
        var.disabled = True
        var = self.fields['year']
        var.disabled = True

        var = self.fields['exam']
        var.disabled = True
        var = self.fields['term']
        var.disabled = True

        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control'})
            self.fields['student'].widget = forms.HiddenInput()
            self.fields['year'].widget = forms.HiddenInput()
            self.fields['exam'].widget = forms.HiddenInput()
            self.fields['term'].widget = forms.HiddenInput()



class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        fields= '__all__'

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self). __init__( *args, **kwargs)
        var = self.fields['school']
        var.disabled = True
        
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control'})
            self.fields['school'].widget = forms.HiddenInput()





class GalleryForm(ModelForm):
    class Meta:
        model= Gallery
        fields= '__all__'
        exclude= ( 'date_created',)

    
    def __init__(self, *args, **kwargs):
        super(GalleryForm, self). __init__( *args, **kwargs)
        var = self.fields['school']
        var.disabled = True
        
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control'})
            self.fields['school'].widget = forms.HiddenInput()



class TeacherForm(ModelForm):
    class Meta:
        model= Teacher
        fields= '__all__'
        exclude= ( 'date_created',)

    
    def __init__(self, *args, **kwargs):
        super(TeacherForm, self). __init__( *args, **kwargs)
        var = self.fields['school']
        var.disabled = True
        
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control'})
            self.fields['school'].widget = forms.HiddenInput()


class MessageForm(ModelForm):
    class Meta:
        model= Message
        fields= '__all__'
        exclude= ( 'date_created',)

    
    def __init__(self, *args, **kwargs):
        super(MessageForm, self). __init__( *args, **kwargs)
        
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control'})



class MyclubForm(ModelForm):
    class Meta:
        model= Myclub
        fields= '__all__'
        exclude= ( 'date_created',)

        
    def __init__(self, *args, **kwargs):
        super(MyclubForm, self). __init__( *args, **kwargs)
        var = self.fields['school']
        var.disabled = True
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control'})
            self.fields['school'].widget = forms.HiddenInput()



class AddClubForm(ModelForm):
    class Meta:
        model= AddtoClub
        fields= '__all__'
        
    def __init__(self, *args, **kwargs):
        super(AddClubForm, self). __init__( *args, **kwargs)
        var = self.fields['student']
        var.disabled = True
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control'})
            self.fields['student'].widget = forms.HiddenInput()


class ClubActivityForm(ModelForm):
    class Meta:
        model= ClubActivity
        fields= '__all__'
        exclude= ( 'date_created',)

    def __init__(self, *args, **kwargs):
        super(ClubActivityForm, self). __init__( *args, **kwargs)
        var = self.fields['myclub']
        var.disabled = True
        var = self.fields['school']
        var.disabled = True
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control'})
            self.fields['school'].widget = forms.HiddenInput()
            self.fields['myclub'].widget = forms.HiddenInput()



class ContactForm(ModelForm):
    class Meta:
        model= Contact
        fields= '__all__'
        exclude= ( 'date_created',)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self). __init__( *args, **kwargs)
        var = self.fields['school']
        var.disabled = True
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control'})
            self.fields['school'].widget = forms.HiddenInput()



# upload document form

class DocumentForm(ModelForm):
    class Meta:
        model= Document
        fields= '__all__'
        exclude= ( 'date_created',)

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self). __init__( *args, **kwargs)
        var = self.fields['school']
        var.disabled = True
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control'})
            self.fields['school'].widget = forms.HiddenInput()


class SchoolForm(ModelForm):
    class Meta:
        model= School
        fields= '__all__'
        exclude= ( 'date_created','school_code',)

    def __init__(self, *args, **kwargs):
        super(SchoolForm, self). __init__( *args, **kwargs)
        var = self.fields['user']
        var.disabled = True
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control'})
            self.fields['user'].widget = forms.HiddenInput()
