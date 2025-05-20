from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, Http404
from django.forms.models import model_to_dict
from .models import Event
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

def event_list_view(request):
    events = Event.objects.all().order_by('-event_date')
    data = []
    for ev in events:
        data.append({
            'id': ev.id,
            'title': ev.title,
            'description': ev.description,
            'event_date': ev.event_date.strftime('%Y-%m-%d %H:%M'),
            'capacity': ev.capacity,
            'created_by': ev.created_by.username,
            'attendees': [u.username for u in ev.attendees.all()]
        })
    return JsonResponse(data, safe=False)


def event_detail_view(request, id):
    try:
        ev = Event.objects.get(id=id)
    except Event.DoesNotExist:
        raise Http404("رویداد پیدا نشد")
    data = model_to_dict(ev)
    data['created_by'] = ev.created_by.username
    data['attendees'] = [u.username for u in ev.attendees.all()]
    data['event_date'] = ev.event_date.strftime('%Y-%m-%d %H:%M')
    return JsonResponse(data)


def event_search_view(request):
    q = request.GET.get('q', '')
    events = Event.objects.filter(title__icontains=q)
    data = [{
        'id': ev.id,
        'title': ev.title,
        'description': ev.description,
        'event_date': ev.event_date.strftime('%Y-%m-%d %H:%M'),
        'created_by': ev.created_by.username
    } for ev in events]
    return JsonResponse(data, safe=False)