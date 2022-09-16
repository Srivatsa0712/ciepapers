from cProfile import label
from tkinter.ttk import LabeledScale
from attr import fields
from django import forms
from django.forms import ModelForm
from matplotlib import widgets
from login2.models import course, faculty
from login2.models import users, committee1,committee,subjects
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create form for faculty
class facultyForm(ModelForm):
    class Meta:
        model = faculty
        fields = ('Username','FirstName','LastName','Email','Password')
        labels={
            'Username':'',
            'FirstName':'',
            'LastName':'',
            'Email':'',
            'Password':'',

        }
        widgets= {
            'Username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your username'}),
            'FirstName':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your FirstName'}),
            
            'LastName':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your LastName'}),
            'Email':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your Email Id'}),
            'Password':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your Password'}),
        }

class usersForm(ModelForm):
    class Meta:
        model = users
        fields='__all__'

class userscForm(ModelForm):
    class Meta:
        model = users
        fields='__all__'

class committee1Form(ModelForm):
    class Meta:
        model = committee1
        fields='__all__'

class courseForm(ModelForm):
    class Meta:
        model= course
        fields ='__all__'
    
class committee1Form(ModelForm):
    class Meta:
        model = committee1
        fields='__all__'

class subjectsForm(ModelForm):
    class Meta:
        model = subjects
        fields='__all__'

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super(RegisterUserForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'