from django.contrib import admin 
from .models import Post 

class PostAdmin(admin.ModelAdmin): 
    list_display = ('title', 'slug', 'created_at', 'updated_on') # Include the updated_on field 
    fields = ['title', 'slug', 'content', 'created_at', 'updated_on'] 
    
    admin.site.register(Post)