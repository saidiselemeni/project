#from django.shortcuts import render
#from rest_framework.decorators import api_view
#from.models import *
#rom.serializers import *
#from rest_framework.response import Response

# Create your views here.
#@api_view(['GET'])
#def getChairPerson(request):
  #  chairper = chairperson.objects.all()
 #   serializer = chairpersonSerializer(chairper, many=True)   
#    return Response(serializer.data)



#from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(["GET" , "POST"])
def get_and_post(request):
    if request.method == "GET":
        chairPerson = chairperson.objects.all()
        serializer = ChairPersonSerializer(chairPerson, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ChairPersonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
       
        
# @api_view(["GET" ,"PUT" ,"DELETE"])
# def chairperson_view(request, id):
#    try:
#       chairPerson






