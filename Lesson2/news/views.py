from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DeleteView

def news_home(request):
    news = Articles.objects.order_by('date')
    return render(request, 'news/new_home.html', {'news': news})

class NewsDetailView(DetailView):
    model= Articles
    template_name = 'news/details_views.html'
    context_object_name = 'article'
    

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html',)
