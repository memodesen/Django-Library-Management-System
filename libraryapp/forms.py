from django import forms  
    

    
class AppRegisterForm(forms.Form) :
           name=forms.CharField()
           surname=forms.CharField()
           email=forms.EmailField()
           password=forms.CharField(widget=forms.PasswordInput)
           username=forms.CharField()
           


class AppLoginForm(forms.Form) :
           username=forms.CharField(max_length=30)
           password=forms.CharField(widget=forms.PasswordInput)
           
           