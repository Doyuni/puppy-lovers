
from django import forms
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.contenttypes.models import ContentType


from .models import Post, Comment, Review
from puppy_sale.models import PetSupply 

from .forms import CommentCreationForm

### Post ###
class PostListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'community/board.html'
    context_object_name = 'post_list'

    queryset = Post.objects.all()

    
class PostDetailView(DetailView):
    model = Post
    template_name = 'community/board_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(commentable_type__model='Post', commentable_id=self.kwargs['pk'])
        return context
    
    def get_object(self):
        post = super().get_object()
        post.hits += 1
        post.save()
        self.view_count = post.hits
        return post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'community/board_create.html'
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.author_name = self.request.user.real_name
        
        return super().form_valid(form)
   

### Review ###
class ReviewListView(ListView):
    model = Review
    paginate_by = 10
    template_name = 'community/review.html'
    context_object_name = 'review_list'

    queryset = Review.objects.all()
    
class ReviewDetailView(DetailView):
    model = Review
    template_name = 'community/review_detail.html'
    context_object_name = 'review'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(commentable_type__model='review', commentable_id=self.kwargs['pk'])
        return context
    
    
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "community/reviewWrite.html"
    
    fields = ['reviewable_id', 'reviewable_name', 'title', 'score', 'description']        
    
    def get_form(self, *args, **kwargs):
        form = super(ReviewCreateView, self).get_form(*args, **kwargs)
        form.fields['reviewable_id'] = \
            forms.ChoiceField(choices=[
                (pet_supply.pk, pet_supply.name) for pet_supply in PetSupply.objects.all()])
        form.fields['reviewable_name'].widget = forms.HiddenInput()

        return form
    
    def form_valid(self, form):
        form.instance.reviewable_type = ContentType.objects.get_for_model(PetSupply)
        
        form.instance.author = self.request.user
        form.instance.author_name = self.request.user.real_name
        
        return super().form_valid(form)
    
def review_comment_create(request, pk):
    if request.method == 'POST':
        form = CommentCreationForm(request.POST)

        if not form.is_valid():
            return redirect("review_detail", pk=pk)

        comment = form.save(commit=False)
        comment.author = request.user
        comment.author_name = request.user.real_name
        
        comment.commentable_id = pk
        comment.commentable_type = ContentType.objects.get_for_model(Review)
        
        comment.save()
        
        return redirect('review_detail', pk=pk)
        
    return redirect('/')

def review(request):
    pass