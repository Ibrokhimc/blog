from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Articles
from django.views.generic.edit import CreateView
# Create your views here.

def LandingPage(request):
    return render(request, 'landingPage.html')

def BlogPage(request):
    articles = Articles.objects.all()
    return render(request, 'pages.html', {'article':articles})

def DetailPage(request, slug):
    post = get_object_or_404(Articles, slug=slug,)


    return render(request, 'detail.html', {'post':post})

def UserView(request):
    return  render(request, 'user.html')

class CreateViewPage(CreateView):
    model = Articles
    template_name = 'newpost.html'
    fields = ('slug','title', 'catelog', 'body', 'photo')
    success_url = reverse_lazy('page:blogpage')


