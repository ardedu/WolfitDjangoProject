from django.shortcuts import render

def programs(request):
    return render(request, 'programs/programs.html')

from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views import View

def is_admin(user):
    return user.is_authenticated and user.is_staff

def index(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'programs/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'programs/detail_view.html'
    context_object_name = 'article'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['author'] = article.author
        return context
@method_decorator(user_passes_test(is_admin, login_url='/news/access'), name='dispatch')
class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'programs/create.html'
    form_class = ArticlesForm
@method_decorator(user_passes_test(is_admin, login_url='/news/access'), name='dispatch')
class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'programs/news_delete.html'
    success_url = '/news/'

@login_required(login_url='/users/login/')
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('news_home')
        else:
            error = 'La forme a été mal remplie'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'programs/create.html', data)

def access(request):
    return render(request, 'programs/perm.html')
# Create your views here.

