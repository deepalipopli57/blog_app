from django.contrib import admin

# Register your models here.
from blogs.models import BlogsModel

class BlogsModelAdmin(admin.ModelAdmin):
    fields = ('title', 'description', )

admin.site.register(BlogsModel, BlogsModelAdmin)