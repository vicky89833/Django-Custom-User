from django.contrib import admin
from .models import NewUser
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea ,TextInput

class UserAdminConfig( UserAdmin):
    
    model = NewUser
    search_fields = ('email', 'user_name',)
    list_filter = ('email', 'user_name',
                   'is_active', 'is_staff')
    ordering= ('-start_date',)
    list_display = ('email', 'user_name', 'is_superuser',
                    'is_active', 'is_staff')
    fieldsets= (
        (None ,{'fields': ('email', 'user_name', )}),
        ('Permissions',{'fields' : ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    
    formfield_overrides = {
        NewUser.about: {'widget':Textarea(attrs = {'rows': 10, 'cols':40})},
        
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':('email', 'user_name',
                      'password1','password2',
                      'is_active', 'is_staff','is_superuser')
            }
        ),
    )
    
    
admin.site.register(NewUser, UserAdminConfig)
