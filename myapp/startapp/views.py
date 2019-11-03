from django.contrib.auth.models import User
from rest_framework import viewsets,mixins
from .models import SousCategory,Category,Product,Oders,Details_Client
from startapp.serializers import UserCommercialSerializer,DetailsSerializerClient,UserClientSerializer,CategorySerializer,ProductSerializer,OrdersSerializer,SousCategorySerializer,MenuSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import FileUploadParser
from rest_framework import filters
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
import json
from django.forms.models import model_to_dict
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.core import serializers
from django.db import connection
import datetime
from django.http import HttpResponse
from rest_framework import status


from django.conf import settings
import os





class UserCommercialViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserCommercialSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        details = Details_Commercial.objects.create(CommercialDetails_id=serializer.data['id'])
        user = User.objects.get(id=serializer.data['id'])
        token = Token.objects.create(user=user)
        return JsonResponse({'User':model_to_dict(user),'Details':model_to_dict(details),'token': token.key})










class UserDetailClientViewSet(viewsets.ModelViewSet):

    queryset = Details_Client.objects.all()
    serializer_class = DetailsSerializerClient





class UserClientViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserClientSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        details = Details_Client.objects.create(ClientDetails_id=serializer.data['id'],Picture=request.data['Picture'])
        user = User.objects.get(id=serializer.data['id'])
        token = Token.objects.create(user=user)
        return JsonResponse({'User':model_to_dict(user),'Details':model_to_dict(details),'token': token.key})








class SousCategoryViewSet(viewsets.ModelViewSet):

    queryset = SousCategory.objects.all()
    serializer_class = SousCategorySerializer



class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class MenuViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = MenuSerializer    


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Product_Commercial_Category','Product_Commercial_SousCategory']





class OrdersViewSet(viewsets.ModelViewSet):

    queryset = Oders.objects.all().order_by('id').reverse()
    serializer_class = OrdersSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Order_Commercial','Remove']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer)

        Oders.objects.create(Order_Product_id=request.data['Order_Product'],Order_Commercial_id=request.data['Order_Commercial'],Order_Table=request.data['Order_Table'],Quantity=request.data['Quantity'],Order_Client_id=request.data['Order_Client'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)





@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def LoginCommercial(request):

    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    user = User.objects.get(id=user.id)
    
    return JsonResponse({'User':model_to_dict(user),'token': token.key})



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def LoginClient(request):

    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    user = User.objects.get(id=user.id)
    details = Details_Client.objects.get(ClientDetails_id=user.id)
    return JsonResponse({'User':model_to_dict(user),'Details':model_to_dict(details),'token': token.key})