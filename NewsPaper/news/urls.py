# from django import views
from django.urls import path
from .views import NewsList, NewsDetail, LoremDetail, PostDelete, PostSearch, SearchHeader, AddPost, PostUpdate
from . import views

urlpatterns = [
   
    path('', NewsList.as_view(), name='news'),
    path('<int:pk>/', LoremDetail.as_view(), name='lorem_post'),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('search_site/', PostSearch.as_view(), name='search_site'),
    path('search_2/', SearchHeader.as_view(), name='search_2'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('<int:pk>/edit_post/', PostUpdate.as_view(), name='edit_post'),
    path('<int:pk>/delete_post/', PostDelete.as_view(), name='delete_post'),
]

