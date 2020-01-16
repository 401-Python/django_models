from django.db import models

# Create your models here.
class Comment(models.Model):
  title = models.CharField(max_length=128)
  body = models.TextField()
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

  def __str__(self):
    return self.title
  
  
