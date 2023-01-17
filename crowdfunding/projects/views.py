from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, generics

from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer

# Create your views here.
class ProjectList(APIView): #project is going to be in long form (this is what is going on under the hood)

    def get(self, request): #using get here #when you get a get requets this is what you do
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True) #telling it we can do many of a thing
        return Response(serializer.data) #we are getting the data out of the serialiser

    def post(self, request): #when you get a post request this is what you do
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk) #pk = the variable we give it is the primary ley
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

class PledgeList(generics.ListCreateAPIView): #pledge is going to be shown in short efficient form (here is your car who carts whats in it)
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

