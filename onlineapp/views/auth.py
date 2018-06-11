from django.views import View
from django.shortcuts import render,get_object_or_404
from onlineapp.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
import ipdb

class SignUpView(View):
    form_class = SignUpForm

    def get(self,request,*args,**kwargs):
        form = SignUpForm()
        return render(request,template_name="signupform.html",context={'form':form})

    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                return redirect('onlineapp:colleges_html')
            else:
                return redirect('onlineapp:signup')


class LoginView(View):
    form_class = LoginForm

    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,template_name='loginform.html',context={'form':form})

    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                return redirect('onlineapp:colleges_html')
            else:
                return redirect('onlineapp:login')

def logout_user(request):
    logout(request)
    return redirect('onlineapp:login')