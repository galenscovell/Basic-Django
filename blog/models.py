
# Include bits from other files
from django.db import models
from django.utils import timezone

# Define Post model (.Model means Django model)
class Post(models.Model):
  # Define properties
  author = models.ForeignKey('auth.User')
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save

  def __str__(self):
    return self.title
