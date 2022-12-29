from django.contrib import admin
from appBackend.models import Category, Expense, Income
# Register your models here.
admin.site.register(Expense)
admin.site.register(Income)

admin.site.register(Category)


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
# list_display=['id','cname','ctype','cdate']
    

