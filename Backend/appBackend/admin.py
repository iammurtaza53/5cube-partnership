from django.contrib import admin
from appBackend.models import Category, Expense, Income,Group,Share
# Register your models here.
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Category)
admin.site.register(Group)
admin.site.register(Share)

