from django.shortcuts import render


# Create your views here.
def index(request):
    page_name = 'Index'
    return render(request, 'myapp/index.html', {'page_name': page_name})


def about(request):
    page_name = 'About'
    return render(request, 'myapp/about.html', {'page_name': page_name})


def news(request):
    page_name = 'News'
    return render(request, 'myapp/news.html', {'page_name': page_name})
