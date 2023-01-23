from rest_framework import serializers

from .models import Project, Pledge

class PledgeSerializer(serializers.ModelSerializer): #doing the serializer no manually
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter'] 
        read_only_fields = ['id', 'supporter']
        if 'anonymous' == 1:
            exclude = ['supporter']

            

# class PledgeSerializer(serializers.ModelSerializer): #doing the serializer no manually
#     class Meta:
#         model = Pledge
#         fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter'] 
#         if 'anonymous' == 1:
#             read_only_fields = ['id']
#             extra_kwargs = {'supporter': {'write_only': True}}
#         else:
#             read_only_fields = ['id', 'supporter']
#             extra_kwargs = {'supporter': {'write_only': False}}

# class PledgeSerializer(serializers.ModelSerializer): #doing the serializer no manually
#     anonymous_conditional_field = serializers.SerializerMethodField()

#     class Meta:
#         model = Pledge
#         fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter'] 
#         read_only_fields = ['id', 'supporter']
    
#     def get_anonymous_conditional_field(self, obj):
#             if obj.anonymous == 1:
#                 return obj.amount


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

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

class ProjectDetailSerializer(ProjectSerializer): #pledges linked to each project split off 
    pledges = PledgeSerializer(many=True, read_only=True)  #reducing the amount of data we are fetching when viewing allprojects     

