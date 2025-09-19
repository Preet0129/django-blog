from django.db import models

# Create your models here.

class About(models.Model):
  about_heading = models.CharField(max_length=25)
  about_description = models.TextField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now = True)

  class Meta:
    verbose_name_plural = "About"

  def __str__(self):
    return self.about_heading
  
class Links(models.Model):
  link_title = models.CharField(max_length=25)
  link_url = models.URLField(max_length = 100)

  class Meta:
    verbose_name_plural = "Link"

  def __str__(self):
    return self.link_title 
  
