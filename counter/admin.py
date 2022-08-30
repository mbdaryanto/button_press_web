from django.http import HttpRequest
from django.contrib import admin
from .models import UserPress, PressCounter


class PressCounterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

class UserPressAdmin(admin.ModelAdmin):

    list_display = ('user', 'at')
    list_filter = ['user', 'at']
    search_fields = ['user', 'at']

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False


admin.site.register(UserPress, UserPressAdmin)
admin.site.register(PressCounter, PressCounterAdmin)
