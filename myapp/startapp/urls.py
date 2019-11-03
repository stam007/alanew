from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from rest_framework.authtoken.views import ObtainAuthToken
from .views import UserCommercialViewSet,LoginCommercial,LoginClient,UserClientViewSet,SousCategoryViewSet,CategoryViewSet,ProductViewSet,OrdersViewSet,MenuViewSet,UserDetailClientViewSet


router = routers.DefaultRouter()

router.register(r'userscommercial', UserCommercialViewSet)
router.register(r'usersclient', UserClientViewSet)
router.register(r'usersclientdetails', UserDetailClientViewSet)

router.register(r'souscategory', SousCategoryViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'produit', ProductViewSet)
router.register(r'orders', OrdersViewSet)






urlpatterns = [

    url('', include(router.urls)),
  
    path('logincommercial/', LoginCommercial),
    path('loginclient/', LoginClient),



]
