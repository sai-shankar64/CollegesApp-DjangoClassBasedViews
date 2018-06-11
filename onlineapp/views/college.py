from django.views import View
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from onlineapp.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
import ipdb

class CollegeView(View):

    def get(self,request,*args,**kwargs):
        colleges=College.objects.all()
        return render(request,template_name='college.html',context={'colleges':colleges})


class CollegeListView(LoginRequiredMixin,ListView):
    login_url='/login/'

    model=College
    context_object_name='colleges'
    template_name = 'colleges.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(CollegeListView,self).get_context_data(**kwargs)
        context['data']=self.model.objects.values('id','name','acronym')
        context.update({'user_permissions':self.request.user.get_all_permissions})
        return context


class CollegeDetailsView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = College
    template_name = 'collegedetails.html'
    def get_object(self,queryset=None):
        return get_object_or_404(College,**self.kwargs)


    def get_context_data(self,**kwargs):
        context=super(CollegeDetailsView,self).get_context_data(**kwargs)
        college=context.get('college')
        students=list(college.student_set.order_by("-mocktest1__total"))
        context.update({
            'students':students,
            'user_permissions':self.request.user.get_all_permissions()
        })
        return context


class CreateCollegeView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'create_college'
    login_url = '/login/'
    model = College
    template_name = 'college_form.html'
    form_class = AddCollege
    success_url = reverse_lazy('onlineapp:colleges_html')


class UpdateCollegeView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required=('change_college')
    login_url = '/login/'
    model=College
    template_name="college_form.html"
    form_class=AddCollege
    success_url = reverse_lazy('onlineapp:colleges_html')

class DeleteCollegeView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = ('delete_college')
    login_url = '/login/'
    model=College
    template_name = "college_confirm_delete.html"
    success_url = reverse_lazy('onlineapp:colleges_html')
