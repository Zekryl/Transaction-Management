from django.contrib import admin
from .models import Transaction
from .models import Category
# from .models import Type

admin.site.register(Transaction)
admin.site.register(Category)
# admin.site.register(Type)
