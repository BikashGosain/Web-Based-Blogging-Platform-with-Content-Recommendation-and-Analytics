from django.contrib import admin
from .models import AboutUs

# Register your models here.
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('about_heading', 'created_at', 'updated_at')  # fields to be displayed in admin panel
    search_fields = ('about_heading',)  # search by about_heading

    def has_add_permission(self, request):
        count = AboutUs.objects.all().count()
        if count == 0:
            return True
        else:
            return False

admin.site.register(AboutUs, AboutUsAdmin)