from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=("id","username","email")
class MovieAdmin(admin.ModelAdmin):
    list_display=("id","creator","timestamp")
class MovieViewAdmin(admin.ModelAdmin):
    list_display=("title","creator_mail")
admin.site.register(User,UserAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(MovieView,MovieViewAdmin)