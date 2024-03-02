from django.contrib import admin
from .models import Drink, User
# Register your models here.
admin.site.register(Drink)


admin.site.site_header = 'Drinks Admin Portal'

admin.site.index_title = 'Welcome to Drinks Dashboard'


# display all fields in the admin   
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone', 'first_name', 'last_name', "is_staff",'date_joined']
  
    list_per_page = 10

admin.site.register(User, UserAdmin)