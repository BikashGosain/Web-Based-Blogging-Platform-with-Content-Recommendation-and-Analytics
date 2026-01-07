from django.db import models

# Create your models here.

class AboutUs(models.Model):
    about_heading = models.CharField(max_length=200)
    about_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heading