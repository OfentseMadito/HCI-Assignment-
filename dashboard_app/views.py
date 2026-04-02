# dashboard_app/views.py
from django.shortcuts import render, get_object_or_404
from report_app.models import Report   # ← Correct import

def dashboard(request):
    reports = Report.objects.all().order_by('-reported_date')
    
    context = {
        'reports': reports,
        'all_count': reports.count(),
        'in_progress': reports.filter(status='in_progress').count(),
        'resolved': reports.filter(status='resolved').count(),
    }
    return render(request, 'dashboard_app/dashboard.html', context)

def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'dashboard_app/report_detail.html', {'report': report})