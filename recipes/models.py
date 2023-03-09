from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))

CATEGORY_CHOICES = (
    ('Meditation', 'Meditation'),
    ('Yoga', 'Yoga'),
    ('Technology', 'Technology'),
    ('Moment', 'Moment'),)

# Model for a post/recipe


class Recipe(models.Model):
    header = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts"
        )
    hero_image = CloudinaryField('image', default='placeholder')
    categories = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default="Meditation")
    summary = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_like', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.header

    def number_of_likes(self):
        return self.likes.count()


# Model for a comment


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('recipe_detail', args=[self.recipe.slug])
