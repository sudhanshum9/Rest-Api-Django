from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):

    def get(self,request,format=None):

        an_apiview= [
            'Uses HTTP response as function (get,put,post,delete)',
            'Is similar to a traditional Django View'

        ]
        return Response({'message': "Hey there",'an_apiview': an_apiview})