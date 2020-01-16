from django.views.generic import ListView, DetailView
from .models import Comment
# Create your views here.
class HomePageView(ListView):
  template_name = 'home.html'
  model = Comment
  context_object_name = 'comments'

class CommentDetailView(DetailView):
  template_name = 'comment_detail.html'
  model = Comment
