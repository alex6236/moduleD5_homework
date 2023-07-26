from datetime import datetime, timezone
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from .models import Post
from django_filters.views import FilterView
from .filters import PostFilter
from .forms import DateFilterForm, TitleFilterForm, TtextFilterForm, UsernameFilterForm, AddPostForm
# =========================
from django.db.models import Q
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now(timezone.utc)
        context['form'] = AddPostForm() 
        return context
# ====================================================    
 
class AddPost(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    form_class = AddPostForm
    permission_required = ('news.add_post' )
    template_name = 'add_post.html'
    success_url = '/news/'
    # login_url = '/accounts/login/'
    login_url = '/signup/login_site/'

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = self.request.user.author
        return super().form_valid(form)
    
    
class PostUpdate(PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = AddPostForm
    permission_required = ('news.change_post')
    template_name = 'edit_post.html'
    success_url = '/news/'

    

class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    permission_required = ('news.delete_post')
    template_name = 'delete_post.html'
    success_url = '/news/'

# ==============================================

class NewsDetail(DetailView):
    model = Post
    template_name ='news_detail.html'
    context_object_name = 'news_detail'
    
class LoremDetail(DetailView):
    model = Post
    template_name ='lorem_post.html'
    context_object_name = 'lorem_post'

class PostSearch(FilterView):
    model = Post
    filterset_class = PostFilter
    template_name = 'search_site.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['filter'] = filter
        results = self.filterset.qs if self.request.GET else Post.objects.none()
        context['results'] = results.order_by('-dataCreation')
        context['date'] = DateFilterForm(self.request.GET or None) 
        context['title'] = TitleFilterForm(self.request.GET or None) 
        context['username'] = UsernameFilterForm(self.request.GET or None) 
        context['text'] = TtextFilterForm(self.request.GET or None) 
        return context

    
class SearchHeader(FilterView):
    model = Post
    template_name = 'search_2.html'
    paginate_by = 2
    # filterset_class = PostFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('q', '')
        if q:  
            multiple_q = Q(
                Q(title__iregex=q) |
                Q(author__authorUser__username__iregex=q) |
                Q(text__iregex=q))
            results = Post.objects.filter(multiple_q).order_by('-id')
            paginator = Paginator(results, self.paginate_by)
            page_number = self.request.GET.get('page')
            context['results'] = paginator.get_page(page_number)
        return context
    
