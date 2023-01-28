from rest_framework import serializers
from .models import CustomUser
# from projects.serializers import ProjectDetailSerializer

# class CustomUserSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     username = serializers.CharField(max_length=150)
#     email = serializers.EmailField()

#     def create(self, validated_data):
#         return CustomUser.objects.create(**validated_data)

class CustomUserSerializer(serializers.ModelSerializer):
    # liked_by = ProjectDetailSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password']
        read_only_fields = ['id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user