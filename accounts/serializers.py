from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Detail, City, Country
from rest_framework import serializers


class MainUserSerializer(serializers.ModelSerializer):
    """
    This class creates a Serializer to serialize the data of a user.

    '''

    Attributes
    ----------
    Meta : user defined type
        a type/class to define the meta-data of this specific 
        Serializer.
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

    
class CitySerializer(serializers.ModelSerializer):
    """
    This class creates a Serializer to serialize the data of a user.

    '''

    Attributes
    ----------
    Meta : user defined type
        a type/class to define the meta-data of this specific 
        Serializer.
    """

    class Meta:
        model = City
        fields = ('name',)


class CountrySerializer(serializers.ModelSerializer):
    """
    This class creates a Serializer to serialize the data of a user.

    '''

    Attributes
    ----------
    Meta : user defined type
        a type/class to define the meta-data of this specific 
        Serializer.
    """

    city = CitySerializer()

    class Meta:
        model = Country
        fields = ('name', 'city')


class UserSerializer(serializers.ModelSerializer):
    """
    This class creates a Serializer to serialize the data of a user.

    '''

    Attributes
    ----------
    Meta : user defined type
        a type/class to define the meta-data of this specific 
        Serializer.
    """

    usr = MainUserSerializer()
    country = CountrySerializer()
    city = CitySerializer()

    class Meta:
        model = Detail
        fields = ('usr', 'gender', 'age', 'country', 'city')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.username = validated_data['usr']['username'],
        instance.first_name = validated_data['usr']['first_name'],
        instance.last_name = validated_data['usr']['last_name'],
        instance.email = validated_data['usr']['email'],
        instance.gender = validated_data['gender'],
        instance.age = validated_data['age'],
        instance.country = validated_data['country'],
        instance.city = validated_data['city']

        
        instance.save()
            
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**{
            'username': data['email'],
            'password': data['password']
            })

        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')