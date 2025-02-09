from django.contrib import admin
from .models import CalendarPlan

class CalendarPlanAdmin(admin.ModelAdmin):
    list_display = ('date', 'class_group', 'subject', 'topic')  # Відображати поле subject

admin.site.register(CalendarPlan, CalendarPlanAdmin)