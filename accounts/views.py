from rest_framework import generics
from rest_framework.response import Response
from .models import Detail, User, Country, City
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .serializers import LoginSerializer, UserSerializer, CountrySerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login


class LoginAPI(generics.GenericAPIView):
    """
    This class creates the API for Login of a user.

    '''

    Attributes
    ----------
    serializer_class : LoginSerializer Class's Object
        a variable to attach a specific Serialezer with this API.
    
    Methods
    -------
    post(request, *args, **kwargs)
        stores the user's data after serializing and validating it.
    """

    serializer_class = LoginSerializer

    def post(self, request):
        """
        Step 1:
            Gets the serialzed data of the user, entered in frontend 
            of API.
        Step 2:
            Stores that data in 'serialzer' variable and validate it.
        Step 3:
            Saves the validated 'data' Object (a dictionary) in the 
            variable 'user'.

        Parameters
        ----------
        request : DRF HTTP POST Request Object
            data entered by the user on the frontend of the DRF
            REST API.

        Returns
        ------
        Dictionary
            a dictionary holding the values of the keys 'token' and 
            'user_id'.
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({
            "token": str(token),
            "user_id": user.id
        })


class LogoutAPI(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        print(request.user.email)
        request.user.auth_token.delete()
        print(request.user.auth_token)
        return Response('User Logged out successfully')

class UserAPI(generics.GenericAPIView):
    """
    This class creates the API for User.

    '''

    Attributes
    ----------
    permission_classes : list
        a list to define who should have access to this API
    serializer_class : UserSerializer Class's Object
        a variable to attach a specific Serialezer with this API
    
    Methods
    -------
    get_object()
        returns value stored in 'user' key of 'request', a DRF HTTP
        POST Object (a dictionary).
    """

    serializer_class = UserSerializer

    def get(self, request, id):
        detail = Detail.objects.get(user=User.objects.get(pk=id))
        usr = User.objects.get(pk=id)
        
        data = {
            'id': usr.id,
            'username': usr.username,
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'email': usr.email,
            'gender': detail.gender,
            'age': detail.age,
            'country': detail.country,
            'city': detail.city

        }

        return Response(data)

    def patch(self, request, id):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user)
        detail = Detail.objects.get(user=User.objects.get(pk=id))
        usr = User.objects.get(pk=id)

        data = {
            'id': usr.id,
            'username': usr.username,
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'email': usr.email,
            'gender': detail.gender,
            'age': detail.age,
            'country': detail.country,
            'city': detail.city

        }


class CountriesAPI(generics.GenericAPIView):
    serializer_class = CountrySerializer

    def get(self, request):
        countries = Country.objects.all()
        full_data = []
        data = {
            'id': 0,
            'name': 'n',
            'cities': []
        }

        for country in countries:
            data['id'] = country.id
            data['name'] = country.name

            cities = City.objects.all()

            for city in cities:
                if city.country.id == data['id']:
                    data['cities'].append({
                        'id': city.id,
                        'name': city.name
                        })
            
        return Response(data)

    def post():
        pass


class SaleStatisticsAPI(generics.GenericAPIView):
    def get():
        pass


class SaleAPI(generics.GenericAPIView):
    def get():
        pass


class UpdateSaleAPI(generics.GenericAPIView):
    def get(self, request, id):
        pass