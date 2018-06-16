from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from onlineapp.models import *
from django.http import HttpResponse, JsonResponse
from onlineapp.serializers.model_serializers import *
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import json

@api_view(['GET'])
@authentication_classes((BasicAuthentication,))
@permission_classes((IsAuthenticated,))
def CollegeListViewApi(request):
    if request.method == 'GET':
        colleges = College.objects.all()
        serializer = CollegeSerializer(colleges, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
@authentication_classes((BasicAuthentication,))
@permission_classes((IsAuthenticated,))
def CreateCollegeViewApi(request):

    if request.method == 'POST':
        data=JSONParser().parse(request)
        serializer = CollegeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['PUT','DELETE'])
@authentication_classes((BasicAuthentication,))
@permission_classes((IsAuthenticated,))
def CollegeChangeViewApi(request, pk):

    try:
        college = College.objects.get(pk=pk)
    except college.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data=JSONParser().parse(request)
        serializer = CollegeSerializer(college, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        college.delete()
        return HttpResponse(status=204)


@api_view(['GET'])
@authentication_classes((BasicAuthentication,))
@permission_classes((IsAuthenticated,))
def CollegeViewApi(request,id):

    if request.method=='GET':
        college=College.objects.filter(pk=id)
        # import ipdb
        # ipdb.set_trace()
        serializer=CollegeSerializer(college,many=True)
        return JsonResponse(serializer.data,safe=False)
