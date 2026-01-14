from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog, Category, Comment
from django.db.models import Q

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


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    comments = Comment.objects.filter(blog=single_blog).select_related('user').prefetch_related('replies')

    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST.get('comment', '').strip() #'comment ' is for in blogs.html textarea name attribute name="comment "
        parent_id = request.POST.get('parent_id')
        
        if comment.comment:
            comment = Comment(
                blog=single_blog,
                user=request.user,
                comment=comment.comment
            )

        if parent_id: 
            comment.parent = Comment.objects.get(id=parent_id)



        comment.save()
        return redirect(request.path)
        # return redirect('blogs', slug=single_blog.slug)
        # return HttpResponse(request.path_info)  # import httpresponse too
# comments in each blog post will be shown in blog detail page
    comments = Comment.objects.filter(blog=single_blog).order_by('-created_at')
    comment_count = comments.count()

    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    results = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        'results': results,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)