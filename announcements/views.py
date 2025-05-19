from django.shortcuts import render

# Create your views here.
# views.py
from django.http import JsonResponse
from django.conf import settings
from .models import Announcement
from django.http import JsonResponse, Http404
from .models import Announcement
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
def announcements_list_view(request):
    announcements = Announcement.objects.all().order_by('-datetime_add')
    data = []

    for ann in announcements:
        data.append({
            "id": ann.id,
            "title": ann.title,
            "content": ann.content,
            "datetime_add": ann.datetime_add.strftime('%Y-%m-%d %H:%M'),
            "image_url": request.build_absolute_uri(ann.image.url) if ann.image else None
        })

    return JsonResponse(data, safe=False)


def announcement_detail_view(request, id):
    try:
        ann = Announcement.objects.get(id=id, status=True)
    except Announcement.DoesNotExist:
        raise Http404("Announcement not found")

    # تبدیل مدل به دیکشنری و حذف image
    data = model_to_dict(ann, exclude=['image'])

    # اضافه کردن URL تصویر به صورت دستی
    data['image_url'] = request.build_absolute_uri(ann.image.url) if ann.image else None

    return JsonResponse(data)



from django.db.models import Q

def announcement_search_view(request):
    query = request.GET.get('q', '')
    results = Announcement.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query),
        status=True
    )

    data = []
    for ann in results:
        item = {
            "id": ann.id,
            "title": ann.title,
            "content": ann.content,
            "datetime_add": ann.datetime_add.strftime('%Y-%m-%d %H:%M'),
            "image_url": request.build_absolute_uri(ann.image.url) if ann.image else None,
        }
        data.append(item)

    return JsonResponse(data, safe=False)




from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

@require_http_methods(["POST", "DELETE"])
@csrf_exempt
def announcement_delete_view(request, id):
    try:
        ann = Announcement.objects.get(id=id)
        ann.delete()
        return JsonResponse({'success': True, 'message': 'Announcement deleted.'})
    except Announcement.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Not found.'}, status=404)