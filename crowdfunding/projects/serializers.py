from rest_framework import serializers

from .models import Project, Pledge
from users.serializers import CustomUserSerializer

class PledgeSerializer(serializers.ModelSerializer): #doing the serializer no manually
    supporter = serializers.SerializerMethodField()
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter'] 
        read_only_fields = ['id']
        
    def get_supporter(self, obj):
        if obj.anonymous:
            return f"mystery gnome enthusiast"
        else:
            return obj.supporter.username
        
    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

# class PledgeSerializer(serializers.ModelSerializer): #doing the serializer no manually
#     class Meta:
#         model = Pledge
#         fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter'] 
#         read_only_fields = ['id']
#         if 'anonymous' == 'true':
#             extra_kwargs = {'supporter': {'write_only': True}}
#         else:
#             read_only_fields = ['id','supporter']
        
#     def create(self, validated_data):
#         return Pledge.objects.create(**validated_data)

#this removes all supporters 
# class PledgeSerializer(serializers.ModelSerializer): #doing the serializer no manually
#     class Meta:
#         model = Pledge
#         fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter'] 
#         read_only_fields = ['id']
#         extra_kwargs = {'supporter': {'write_only': True}}

#     def create(self, validated_data):
#         return Pledge.objects.create(**validated_data)   
    

#none of this works

# class DynamicFieldsModelSerializer(serializers.ModelSerializer):
#     """
#     A ModelSerializer that takes an additional `fields` argument that
#     controls which fields should be displayed.
#     """

#     def __init__(self, *args, **kwargs):
#         # Don't pass the 'fields' arg up to the superclass
#         fields = kwargs.pop('fields', None)

#         # Instantiate the superclass normally
#         super().__init__(*args, **kwargs)

#         if fields is not None:
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)

# class PledgeSerializer(serializers.ModelSerializer): #doing the serializer no manually
#     class Meta:
#         model = Pledge
#         if 'anonymous' == 1:
#             fields = ['id', 'amount', 'comment', 'anonymous', 'project'] 
#             read_only_fields = ['id']
#         else:
#             fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter'] 
#             read_only_fields = ['id', 'supporter']
        
#     def create(self, validated_data):
#         return Pledge.objects.create(**validated_data)


# class PledgeSerializer(serializers.ModelSerializer): #doing the serializer no manually
#     class Meta:
#         model = Pledge
#         fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter'] 
#         read_only_fields = ['id', 'supporter']
#         if 'anonymous' == 1:
#             exclude = ['supporter']

            

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
    total = serializers.ReadOnlyField()
    
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
    liked_by = CustomUserSerializer(many=True, read_only=True)

class PledgeDetailSerializer(PledgeSerializer):
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter'] 
        read_only_fields = ['id']
