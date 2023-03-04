from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .forms import CommentForm
from .views import *

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/',  views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name= 'delete_comment'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(), name='edit_comment'),
    path('search', views.search, name='search'),
]