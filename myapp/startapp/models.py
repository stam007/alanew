from django.db import models
from django.contrib.auth.models import User


from django.core.validators import MinLengthValidator
from multiselectfield import MultiSelectField

from django.contrib.postgres.fields import ArrayField


#from django.contrib.postgres.fields import JSONField

import jsonfield



class Category(models.Model):
    
    Category_Commercial =models.ForeignKey(User, related_name='category_for_commercial',on_delete=models.CASCADE)
    Category_Name =  models.TextField(null=True,blank=True,default=None)








class SousCategory(models.Model):
    
    SousCategory_Commercial =models.ForeignKey(Category, related_name='souscategory_for_commercial',on_delete=models.CASCADE)
    SousCategory_Name =  models.TextField(null=True,blank=True,default=None)    





class Product(models.Model):
    
    Product_Commercial_SousCategory = models.ForeignKey(SousCategory, related_name='product_for_commercial_souscategory',on_delete=models.CASCADE)

    Product_Commercial_Category = models.ForeignKey(Category, related_name='product_for_commercial_category',on_delete=models.CASCADE)

    Product_Name =  models.TextField(null=True,blank=True,default=None)
    Description =  models.TextField(null=True,blank=True,default=None)
   
    Price = models.IntegerField(blank=True,null=True)


    Color = jsonfield.JSONField(null=True,blank=True,default=None)

    Demonsion = jsonfield.JSONField(null=True,blank=True,default=None)
  
    Image1 = models.FileField(blank=True, null=True,default=None)
    Image2 = models.FileField(blank=True, null=True,default=None)
    Image3 = models.FileField(blank=True, null=True,default=None)
    Image4 = models.FileField(blank=True, null=True,default=None)


   
   









class Oders(models.Model):
    
    Order_Commercial =models.ForeignKey(User, related_name='order_for_commercial',on_delete=models.CASCADE)
    Order_Product = models.ForeignKey(Product, related_name='order_for_product',blank=True,null=True,on_delete=models.CASCADE)
    Order_Client = models.ForeignKey(User, related_name='order_for_client',blank=True,null=True,on_delete=models.CASCADE)
    Order_No_Client = jsonfield.JSONField(null=True,blank=True,default=None)
    Color =  models.TextField(null=True,blank=True,default=None)
    Demonsion =  models.TextField(null=True,blank=True,default=None)
    Quantity = models.IntegerField(blank=True,null=True,default=None)
    Price = models.IntegerField(blank=True,null=True,default=None)
    Remove = models.BooleanField(default=False,blank=True,null=True)
    Confirm = models.BooleanField(default=False,blank=True,null=True)
    See = models.BooleanField(default=False,blank=True,null=True)       

class Details_Client(models.Model):
    ClientDetails = models.OneToOneField(User, related_name='details_client', on_delete=models.CASCADE)
    Picture = models.TextField(null=True,blank=True,default=None)    
    Email = models.TextField(null=True,blank=True,default=None)
    Adress = models.TextField(null=True,blank=True,default=None)
    First_Name = models.TextField(null=True,blank=True,default=None)
    Last_Name = models.TextField(null=True,blank=True,default=None)
    Phone = models.CharField('Phone Number', max_length=8, validators=[MinLengthValidator(8)], unique= True,blank=True, null=True)

    Completed = models.BooleanField(default=False,blank=True,null=True) 
        