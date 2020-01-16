from django.urls import path
from.views import HomePageView, CommentDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('comment/<int:pk>', CommentDetailView.as_view(), name='comment_detail'),
    
]