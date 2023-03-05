from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import *
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

# View for home page posts


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

# View for main post page in detail


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            messages.add_message(request,
                                 messages.INFO, 'Thank you for your comment!')
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

# View for liking a post


class RecipeLike(LoginRequiredMixin, View):
    """
    Like/Unlike posts
    """
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
            messages.success(request, 'You have unliked this post, thanks!')
        else:
            recipe.likes.add(request.user)
            messages.success(request, 'You have liked this post, thanks!')
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))

# View for deleting logged in user comment


@login_required
def delete_comment(request, comment_id):
    """ Method to delete a comment
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, 'Your comment was deleted successfully')
    return HttpResponseRedirect(reverse(
        'recipe_detail', args=[comment.recipe.slug]))

# View for editing logged in user comment


class EditComment(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit comment
    """
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    success_message = 'Your comment was successfully updated'

# View for searching


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        recipes = Recipe.objects.filter(content__contains=searched)

        return render(request, 'search.html',
                      {'searched': searched, 'recipes': recipes})
    else:
        return render(request, 'search.html', {})
