from django.contrib import admin
from .models import SocialLinks

# Register your models here.

class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ('platform', 'link', 'created_at', 'updated_at')  # fields to be displayed in admin panel
    search_fields = ('platform',)  # search by platform name

admin.site.register(SocialLinks, SocialLinksAdmin)