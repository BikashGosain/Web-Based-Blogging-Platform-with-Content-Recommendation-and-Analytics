from django.shortcuts import render, redirect
from blogs.models import Blog, Category
from about_us.models import AboutUs
from .forms import RegistrationForm

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

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
        
            # You can add a success message or redirect to login page
    context = {
        'form': form,
        }
    return render(request, 'register.html', context)