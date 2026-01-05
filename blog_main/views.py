from django.shortcuts import render
from blogs.models import Blog, Category

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='Published')
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-created_at')
    context = {
        # 'categories': categories, # removed as we are using context processor for categories
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'home.html', context)