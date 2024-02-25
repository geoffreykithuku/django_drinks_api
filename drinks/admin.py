from django.contrib import admin
from .models import Drink
# Register your models here.
admin.site.register(Drink)

admin.site.site_header = 'Drinks Admin Portal'

admin.site.index_title = 'Welcome to Drinks Dashboard'

