from django import forms
from onlineapp.models import *

class AddCollege(forms.ModelForm):
    class Meta:
        model=College
        exclude=['id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'College Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Location'}),
            'acronym': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Acronym'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Contact'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        exclude=['id','dob','college']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'db_folder':forms.TextInput(attrs={'class':'form-control','placeholder':'DB_Folder name'}),
            'dropped_out':forms.CheckboxInput(attrs={'class':'checkbox'}),
        }


class MockTest1Form(forms.ModelForm):
    class Meta:
        model=MockTest1
        exclude={'id','total','student'}
        widgets = {
            'problem1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'score in problem1'}),
            'problem2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'score in problem2'}),
            'problem3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'score in problem3'}),
            'problem4': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'score in problem4'}),
            'problem4': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'score in problem4'}),
        }