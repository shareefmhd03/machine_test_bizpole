
from django.contrib import admin
from .models import Activity,User

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['activity_name', 'user']
    search_fields = ['activity_name', 'user__username']

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

admin.site.register(Activity)
admin.site.register(User)
