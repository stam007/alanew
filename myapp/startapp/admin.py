from django.contrib import admin
from .models import Oders,Product,Category,SousCategory

# Register your models here.

admin.site.register(SousCategory)
admin.site.register(Oders)
admin.site.register(Product)
admin.site.register(Category)

