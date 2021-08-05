from django.contrib import admin

from .models import Category, Post, Comment, Reply

@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','published','status')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Reply)