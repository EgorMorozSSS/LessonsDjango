from django.shortcuts import render

def news_home(request):
    return render(request, 'news/new_home.html')
# Create your views here.
