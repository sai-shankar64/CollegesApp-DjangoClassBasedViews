from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from onlineapp.forms import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
import ipdb

class CreateMockTest1View(CreateView):
    model=MockTest1
    form_class=MockTest1Form

class CreateStudentView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'create_student'
    login_url = '/login/'
    model = Student
    template_name = "student_form.html"
    form_class = StudentForm

    def get_context_data(self, **kwargs):
        context=super(CreateStudentView,self).get_context_data(**kwargs)
        student_form=context.get('form')
        test_form=MockTest1Form
        context.update({'student_form':student_form,'test_form':test_form})
        return context

    def post(self, request, *args, **kwargs):
        student_form=StudentForm(request.POST)
        test_form = MockTest1Form(request.POST)
        college=get_object_or_404(College,pk=kwargs.get('id'))

        if student_form.is_valid():
            new_student = student_form.save(commit=False)
            new_student.college=college
            new_student.save()

            if test_form.is_valid():
                new_student_marks=test_form.save(commit=False)
                new_student_marks.student=new_student
                new_student_marks.total=sum(test_form.cleaned_data.values())
                # ipdb.set_trace()
                new_student_marks.save()
        return redirect('onlineapp:college_details',**kwargs)

class UpdateStudentView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'change_student'
    login_url = '/login/'
    model = Student
    template_name = "student_form.html"
    form_class = StudentForm

    def get_context_data(self, **kwargs):
        context=super(UpdateStudentView,self).get_context_data(**kwargs)
        student_form=context.get('student')
        test_form=MockTest1Form(instance=student_form.mocktest1)
        context.update({'student_form':context.get('form'),'test_form':test_form})
        return context

    def post(self, request, *args, **kwargs):
        college=get_object_or_404(College,pk=kwargs.get('id'))
        # student_instance = get_object_or_404(Student,pk=kwargs.get('pk'))
        # marks_instance = get_object_or_404(MockTest1,student_id=kwargs.get('pk'))
        student_instance=Student.objects.get(pk=kwargs.get('pk'))
        student_form=StudentForm(request.POST,instance=student_instance)
        test_form = MockTest1Form(request.POST,instance=student_instance.mocktest1)
        mocktest_form=test_form.save(commit=False)
        mocktest_form.total = sum(test_form.cleaned_data.values())
        student_form.save()
        mocktest_form.save()
        return redirect('onlineapp:college_details',id=kwargs.get("id"))

class DeleteStudentView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'delete_student'
    login_url = '/login/'
    model=Student
    success_url = reverse_lazy('onlineapp:colleges_html')

    def get(self,request,*args,**kwargs):
        return self.post(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        self.delete(request,*args,**kwargs)
        return redirect('onlineapp:college_details',id=kwargs.get('id'))

