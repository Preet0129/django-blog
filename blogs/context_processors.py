from .models import Category
from assignments.models import Links

def get_categories(request):
  categories = Category.objects.all()
  return dict( categories=categories)

def get_social_links(request):
  social_links = Links.objects.all()
  return dict(social_links=social_links)