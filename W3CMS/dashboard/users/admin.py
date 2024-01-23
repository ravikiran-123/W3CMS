from django.contrib import admin
from dashboard.users.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea



class UserAdminConfig(UserAdmin):
	model = CustomUser
	search_fields = ('email','first_name','last_name','gender')
	list_filter = ('email','first_name','last_name','gender','is_active','is_staff')
	ordering = ('-dob',)
	list_display=('username','email','first_name','last_name','gender','is_active','is_staff','created_at','updated_at')

	fieldsets=(
			(None,{'fields':('username','email', 'first_name','last_name','gender','avatar','dob','password')}),
			('Permissions',{'fields':('is_staff','is_active','is_superuser','groups','user_permissions')}),
			('Personal',{'fields':('phone_number','facebook_url','twitter_url','linkedin_url','about',)}),
		)

	formfield_overrides = {
		CustomUser.about: {'widget': Textarea(attrs={'rows':10,'cols':40})},
	}

	add_fieldsets = (
	(None,{
		'classes':('wide',),
		'fields':('username','email','phone_number','first_name','last_name','gender','avatar','dob','password1','password2','is_active','is_staff','groups','user_permissions')
		}
		),
	)

admin.site.register(CustomUser,UserAdminConfig)

# Register your models here.
