from django.contrib import admin
from .models import Users
from .models import Books

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
       list_display = ("name","surname","username")


admin.site.register(Users,UsersAdmin)
admin.site.register(Books)



                  