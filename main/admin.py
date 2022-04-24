from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from main.models import CustomUser as User


class QuestionAdmin(admin.ModelAdmin):
    list_display=('title','user')
    search_fields=('title','detail')
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)

class CommentAdmin(admin.ModelAdmin):
    list_display=('answer','comment')
admin.site.register(Comment,CommentAdmin)

class UpvoteAdmin(admin.ModelAdmin):
    list_display=('answer','user')
admin.site.register(UpVote,UpvoteAdmin)

class DownvoteAdmin(admin.ModelAdmin):
    list_display=('answer','user')
    
admin.site.register(DownVote,DownvoteAdmin)

admin.site.register(CustomUser)
