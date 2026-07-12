import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import SOSAlert


def trigger_sos(request):
    """Student-facing page with the SOS button."""
    return render(request, 'sos/trigger.html', {
        'location_choices': SOSAlert.LOCATION_CHOICES
    })


@csrf_exempt
@require_POST
def create_sos_alert(request):
    """
    API endpoint called via AJAX (fetch) when student presses SOS.
    Also accepts a 'synced_from_offline' flag when a queued offline
    alert is being synced later.
    """
    try:
        data = json.loads(request.body)
        location = data.get('location')
        synced = data.get('synced_from_offline', False)

        if location not in dict(SOSAlert.LOCATION_CHOICES):
            return JsonResponse({'success': False, 'error': 'Invalid location'}, status=400)

        alert = SOSAlert.objects.create(location=location, synced_from_offline=synced)
        return JsonResponse({'success': True, 'id': alert.id})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


def captain_dashboard(request):
    """Captain-facing live dashboard, polls for new alerts."""
    return render(request, 'sos/captain_dashboard.html')


def get_active_alerts(request):
    """
    API endpoint the captain dashboard polls every few seconds
    to simulate real-time broadcast.
    """
    alerts = SOSAlert.objects.filter(resolved=False).order_by('-triggered_at')[:20]
    data = [{
        'id': a.id,
        'location': a.get_location_display(),
        'triggered_at': a.triggered_at.strftime('%H:%M:%S'),
        'synced_from_offline': a.synced_from_offline,
    } for a in alerts]
    return JsonResponse({'alerts': data})


@csrf_exempt
@require_POST
def resolve_alert(request, alert_id):
    try:
        alert = SOSAlert.objects.get(id=alert_id)
        alert.resolved = True
        alert.save()
        return JsonResponse({'success': True})
    except SOSAlert.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Alert not found'}, status=404)