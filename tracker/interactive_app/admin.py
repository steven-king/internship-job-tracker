from django.contrib import admin
from interactive_app.models import UserProfile, User, Organization, City

admin.site.register(UserProfile)

class UserAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(User, UserAdmin)

class OrganizationAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Organization, OrganizationAdmin)

class CityAdmin(admin.ModelAdmin):
	search_fields = ('city',)

admin.site.register(City, CityAdmin)
