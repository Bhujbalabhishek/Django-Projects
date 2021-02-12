from django.contrib import admin
from .models import Posts
# Register your models here.

admin.site.register(Posts)

admin.site.site_header = "Django Prohject Posts and Blogs"


