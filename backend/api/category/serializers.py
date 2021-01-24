from rest_framework import serializers


from .models import Category


class CategorySerializer(serializers.Serializer):


    class Meta:

        # declare what model we want to use to generate json
        model = Category
        field = ('name', 'description')

        # name = serializers.CharField(max_length =  20)
        # description = serializers.CharField(max_length = 20)