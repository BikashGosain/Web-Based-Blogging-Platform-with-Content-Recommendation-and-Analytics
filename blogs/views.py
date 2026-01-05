from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog, Category

# Create your views here.

def posts_by_category(request, category_id):
    # Logic to fetch posts by category_id
    posts = Blog.objects.filter(category=category_id, status='Published')
    # for check it category exists if not redirect to home

    try:
        category = Category.objects.get(id=category_id)
    except:
        return redirect('home')

    # # (remember to create 404.html page for 404 error but for 5050 error create errorcode.html)for get object or 404 error page if category not found
    # # for this to apply and show 404error.html page made changes in settings.py file debug = False and allowed host = ['*']
    # category = get_object_or_404(Category, id=category_id)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)