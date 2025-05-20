from django.forms import model_to_dict
from django.http import Http404, JsonResponse
from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def article_list_view(request):
    articles = Article.objects.filter(status='approved').order_by('-datetime_add')
    data = []
    for art in articles:
        data.append({
            'id': art.id,
            'title': art.title,
            'text': art.text,
            'datetime_add': art.datetime_add.strftime('%Y-%m-%d %H:%M'),
            'author': art.author.username,
            'status': art.get_status_display(),
        })
    return JsonResponse(data, safe=False)


def article_detail_view(request, id):
    try:
        art = Article.objects.get(id=id, status='approved')
    except Article.DoesNotExist:
        raise Http404("Article not found")
    data = model_to_dict(art)
    data['author'] = art.author.username
    data['status'] = art.get_status_display()
    return JsonResponse(data)


def article_search_view(request):
    q = request.GET.get('q', '')
    articles = Article.objects.filter(title__icontains=q, status='approved')
    data = [{'id': a.id, 'title': a.title,'text':a.text,'author':a.author.first_name+' '+a.author.last_name,'date':a.datetime_add} for a in articles]
    return JsonResponse(data, safe=False)

# ساخت مقاله
@csrf_exempt
def article_create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return JsonResponse({'message': 'مقاله با موفقیت ایجاد شد'})
        return JsonResponse(form.errors, status=400)
    return JsonResponse({'message': 'فقط متد POST پشتیبانی می‌شود'}, status=405)


@csrf_exempt
def article_edit_view(request, id):
    try:
        article = Article.objects.get(id=id, author=request.user)
    except Article.DoesNotExist:
        return JsonResponse({'error': 'مقاله پیدا نشد'}, status=404)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'ویرایش با موفقیت انجام شد'})
        return JsonResponse(form.errors, status=400)
    return JsonResponse({'message': 'فقط متد POST پشتیبانی می‌شود'}, status=405)
# حذف مقاله
@csrf_exempt
def article_delete_view(request, id):
    try:
        art = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return JsonResponse({'error': 'Article not found'}, status=404)

    art.delete()
    return JsonResponse({'success': True})