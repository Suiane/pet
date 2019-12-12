from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import TemplateView

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['titulo','autor','texto']

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['titulo','texto']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('listagem')

class HomePageView(TemplateView):
    model = Post
    template_name = 'home.html'
    
class ListagemView(ListView):
    model = Post
    template_name = 'listagem.html'
    context_object_name = 'lista'

class PostagemDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class HomeUserPageView(TemplateView):
    model = Post
    template_name = 'homeuser.html'

class HomeEmpresaPageView(TemplateView):
    model = Post
    template_name = 'homempresa.html'

class CadastroPageView(TemplateView):
    model = Post
    template_name = 'cadastro.html'