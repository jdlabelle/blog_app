from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """Represent a blog category"""
    name = models.CharField(max_length=50)

    def __str__(self):
        """Display a string representation of the model"""
        return self.name

class Post(models.Model):
    """Represent an individual blog post within a blog category"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def truncated_text(self, length=200):
        if len(self.body) > length:
            return f"{self.body[:length]}..."
        return self.body

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        """Display a string representation of the blog post"""
        # if len(self.body) > 50:
        #     summary = f"{self.body[0:50]}..."
        # else:
        #     summary = self.body 

        return self.title
