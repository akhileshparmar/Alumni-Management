from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth.models import User, Group
# Register your models here.

admin.site.site_title = "Sage University"
admin.site.site_header = "Sage University Alumni Portal"

admin.site.index_title = ""

class AlumniAdmin(admin.ModelAdmin):
    search_fields = ('Firstname', 'Enrollment_no', 'Scholar_no')
    list_display = ('Firstname', 'Enrollment_no', 'Scholar_no')
    list_filter = ('Year','Course','Branch')


class CustomUserAdmin(UserAdmin):
    list_display = ('id','first_name','last_name','is_active')
    list_filter = ['is_active','date_joined','is_superuser']


class EFA(admin.ModelAdmin):
    list_display = ('User_id','Date')
    list_filter = ['Date']

class Feed_back(admin.ModelAdmin):
    list_display = ('User_id','Date')
    list_filter = ['Date']

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Alumni, AlumniAdmin)
admin.site.register(Notice)
admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(Job)
admin.site.register(Email_From_Alumni, EFA)
admin.site.register(Feedback, Feed_back)

admin.site.register(Email_To_Alumni)

admin.site.unregister(Group)
