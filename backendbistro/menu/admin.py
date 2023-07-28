from django.contrib import admin

from .models import Menu_Item, Category, Cuisine, Ingredient


admin.site.register(Menu_Item) #Adds to Admin site
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Ingredient)

