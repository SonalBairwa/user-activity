from django.contrib import admin

from user_activity import models


class UserAdmin(admin.ModelAdmin):
	list_display = ('id', 'real_name', 'tz', 'added_on', 'updated_on',)
	list_filter = ('tz',)
	search_fields = ('real_name',)
	readonly_fields = ('id',)

class UserActivityAdmin(admin.ModelAdmin):
	select_related = ('user',)
	list_display = ('id', 'start_time', 'end_time', 'user', 'added_on', 'updated_on',)
	list_filter = ('user',)

admin.site.register(models.UserModel, UserAdmin)
admin.site.register(models.UserActivityModel, UserActivityAdmin)