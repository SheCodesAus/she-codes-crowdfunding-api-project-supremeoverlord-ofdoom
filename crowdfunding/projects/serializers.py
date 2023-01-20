from rest_framework import serializers

from .models import Project, Pledge

class PledgeSerializer(serializers.ModelSerializer): #doing the serializer no manually
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner_id')
    #pledges = PledgeSerializer(many=True, read_only=True) #so we can see the pledges for each project

    def create(self, validated_data):
        return Project.objects.create(**validated_data) #returns key values pairs - title = string, descrption = value ect


class ProjectDetailSerializer(ProjectSerializer): #pledges linked to each project split off 
    pledges = PledgeSerializer(many=True, read_only=True)  #reducing the amount of data we are fetching when viewing allprojects     

