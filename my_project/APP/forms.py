from django import forms 
from .models import Student
from .models import Book 


class Studentform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    
    
class Studentform1(forms.ModelForm):
    class Meta :
        model=Student
        fields="__all__"
        
class Bookform(forms.ModelForm):
    class Meta:
        model=Book 
        fields="__all__"
    