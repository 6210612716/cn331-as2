from django.contrib import admin
from .models import Course, Quota

# Register your models here.

# admin.site.register(Course)
# admin.site.register(Quota)

class CourseAdmin(admin.ModelAdmin):
    @admin.action(description='Mark selected courses status as OPENED')
    def open_course(modeladmin, request, queryset):
        queryset.update(status=True)

    @admin.action(description='Mark selected courses status as CLOSED')
    def close_course(modeladmin, request, queryset):
        queryset.update(status=False)
        
    list_display = ['c_code', 'c_name', 'semester', 'year', 'quota', 'status']
    ordering = ['c_name']
    actions = [open_course, close_course, ]

admin.site.register(Course, CourseAdmin)

class QuotaAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Quota, QuotaAdmin)
