from django.shortcuts import render
from blogs.models import Blog, Category
from about_us.models import AboutUs

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='Published')
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-created_at')

    # Fetch About Us information
    try:
        about = AboutUs.objects.get()
    except:
        about = None

    context = {
        # 'categories': categories, # removed as we are using context processor for categories
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html', context)