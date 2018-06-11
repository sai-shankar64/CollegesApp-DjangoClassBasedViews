from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from onlineapp.views import *

app_name = 'onlineapp'

urlpatterns = [
    path('signup/',SignUpView.as_view(),name="signup"),
    path("login/",LoginView.as_view(),name="login"),
    path("logout",logout_user,name="logout"),
    path("colleges/",CollegeListView.as_view(),name="colleges_html"),
    path("colleges/<int:id>",CollegeDetailsView.as_view(),name="college_details"),
    path("colleges/add",CreateCollegeView.as_view(),name="college_form"),
    path("colleges/update/<int:pk>",UpdateCollegeView.as_view(),name="update_college"),
    path("colleges/delete/<int:pk>",DeleteCollegeView.as_view(),name="delete_college"),
    path("colleges/<int:id>/add",CreateStudentView.as_view(),name="student_form"),
    path("colleges/<int:id>/update/<int:pk>",UpdateStudentView.as_view(),name="update_student"),
    path("colleges/<str:acronym>",CollegeDetailsView.as_view(),name="college_details"),
    path("colleges/<int:id>/delete/<int:pk>",DeleteStudentView.as_view(),name="delete_student")
]
