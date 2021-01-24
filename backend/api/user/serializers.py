from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes, permission_classes

from .models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):

    # create these two methods create and update to save data into database

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        # return a key-value pair ????
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    # note in update method we already have the instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instace, attr, value)

        instance.save()
        return instance

    class Meta:
        model = CustomUser

        # add your extra parameters that you want to add or modify
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('name', 'email', 'password', 'phone', 'gender',
                  'is_active', 'is_staff', 'is_superuser')
