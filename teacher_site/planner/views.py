from django.shortcuts import render
from .models import CalendarPlan

def calendar_view(request):
    class_group = request.GET.get('class_group')
    subject = request.GET.get('subject')
    plans = CalendarPlan.objects.all().order_by('date')

    # Фільтрація за класом
    if class_group:
        plans = plans.filter(class_group=class_group)

    # Фільтрація за предметом
    if subject:
        plans = plans.filter(subject=subject)

    return render(request, 'planner/calendar.html', {'plans': plans})