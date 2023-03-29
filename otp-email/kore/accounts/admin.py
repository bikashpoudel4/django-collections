from django.contrib import admin
from accounts.models import UserProfiile

#REGISTER MODELS 

# admin.site.register(UserProfiile)

class UserProfiileAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['username', 'email', 'is_active','is_admin', 'is_staff', 'city', 'is_confirmed']
admin.site.register(UserProfiile, UserProfiileAdmin)
