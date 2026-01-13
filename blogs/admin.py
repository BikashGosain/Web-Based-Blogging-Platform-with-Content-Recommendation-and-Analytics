from django.contrib import admin
from .models import Category, Blog, Comment

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # auto fill slug field from title field
    list_display = ('title', 'author', 'category', 'status', 'is_featured', 'created_at')  # fields to be displayed in admin panel
    search_fields = ( 'id', 'title', 'category__category_name', 'status')  # search by title and author's username
    list_editable = ('is_featured', 'status', 'category')  # make is_featured and status editable in list display

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)