from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_average', 'display_top_score')

    def display_average(self, obj):
        return obj.get_average_score()
    display_average.short_description = 'Average Score'

    def display_top_score(self, obj):
        return obj.get_top_score()
    display_top_score.short_description = 'Top Score'

admin.site.register(Student, StudentAdmin)
