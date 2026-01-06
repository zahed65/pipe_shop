from django.shortcuts import render
from .models import Category, MediaItem

def index(request):
    return render(request, 'catalog/index.html')

def about(request):
    return render(request, 'catalog/about.html')
def sample(request):
    return render(request, 'catalog/sample.html')
def contact(request):
    return render(request, 'catalog/contact.html')

def sample_view(request):
    category = request.GET.get('cat')       # project OR monaghese
    media_type = request.GET.get('type')    # photo OR video

    items = MediaItem.objects.all()

    # فیلتر دسته‌بندی بر اساس فیلد name
    if category:
        items = items.filter(category__name=category)

    # فیلتر نوع رسانه
    if media_type:
        items = items.filter(media_type=media_type)

    return render(request, 'catalog/sample.html', {
        'items': items,
    })