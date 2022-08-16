from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=("id","username","email")
class MovieAdmin(admin.ModelAdmin):
    list_display=("id","creator","timestamp","content")
admin.site.register(User,UserAdmin)
admin.site.register(Movie,MovieAdmin)