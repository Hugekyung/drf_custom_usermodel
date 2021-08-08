from rest_framework import serializers

from accountapp import models


class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MyUser
        fields = ('id', 'email', 'name', 'nickname', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.MyUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            nickname=validated_data['nickname'],
            password=validated_data['password']
        )

        return user