from django.contrib.auth.models import User

from rest_framework import serializers
from startapp.models import Category,SousCategory,Product,Oders,Details_Client
from rest_framework.response import Response
from django.http import JsonResponse

from django.forms.models import model_to_dict



class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields =  '__all__'





class SousCategorySerializer(serializers.ModelSerializer):
    #product_for_commercial_souscategory = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = SousCategory
        fields =  '__all__'

class CategorySerializer(serializers.ModelSerializer):
    souscategory_for_commercial = SousCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields =  '__all__'
        








class UserCommercialSerializer(serializers.ModelSerializer):
    
  
    category_for_commercial = CategorySerializer(many=True, read_only=True)
  
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name','last_name','category_for_commercial')
        extra_kwargs ={'password':{'write_only': True , 'required':True}}

    def create(self, validated_data):
          
           user=User.objects.create_user(**validated_data)
           
           return user







class OrdersSerializer(serializers.ModelSerializer):

  
    class Meta:
        model = Oders
        fields =  '__all__'

    Order_Product = ProductSerializer(read_only=True) 





class DetailsSerializerClient(serializers.ModelSerializer):
   
    class Meta:
        model = Details_Client
        fields =  '__all__'



class UserClientSerializer(serializers.ModelSerializer):
    details_client = DetailsSerializerClient(many=False, read_only=True)
    
    class Meta:
        model = User
        #fields =  '__all__'
        fields = ('id', 'username', 'email', 'password','first_name','last_name','details_client')
        extra_kwargs ={'password':{'write_only': True , 'required':True}}

    def create(self, validated_data):
          
           user=User.objects.create_user(**validated_data)
           
           return user  


class MenuSerializer(serializers.ModelSerializer):
    #product_for_commercial_category = ProductSerializer(many=True, read_only=True )

    product_for_commercial_category = serializers.SerializerMethodField()


   
    
    class Meta:
        model = Category
        fields =  '__all__'


    def get_product_for_commercial_category(self, category):
        qs = category.product_for_commercial_category.all()[:4]
        return ProductSerializer(qs, many=True, read_only=True).data               