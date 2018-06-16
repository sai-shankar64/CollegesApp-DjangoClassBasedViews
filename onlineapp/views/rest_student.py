from onlineapp.serializers.model_serializers import *
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# @api_view(['GET'])
# def StudentsOfCollegeViewApi(request,id):
#     if request.method=='GET':
#         college=College.objects.get(pk=id)
#         student=Student.objects.filter(college=college)
#         serializer=StudentSerializer(student,many=True)
#         return JsonResponse(serializer.data,safe=False)
#
# @api_view(['GET'])
# def StudentsMarksViewApi(request,id):
#     if request.method=='GET':
#         result=Student.objects.filter(college_id=id)
#         serializer=StudentDetailsSerializer(result,many=True)
#         return JsonResponse(serializer.data,safe=False)

class StudentsofCollegeViewApi(permissions.BasePermission,APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self,request,id,format=None):
        result=Student.objects.filter(college_id=id)
        serializer=StudentSerializer(result,many=True)
        return Response(serializer.data)

    def post( self, request,id, format=None):
        import ipdb
        ipdb.set_trace()
        # print("hello world")
        serializer = StudentDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentsMarksofCollegeViewApi(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self,request,id,format=None):
        result=Student.objects.filter(college_id=id)
        serializer=StudentDetailsSerializer(result,many=True)
        return Response(serializer.data)

class StudentViewApi(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self,request,id,pk,format=None):
        result=Student.objects.filter(college_id=id,id=pk)
        serializer=StudentDetailsSerializer(result,many=True)
        return Response(serializer.data)

