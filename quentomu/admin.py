from django.contrib import admin
from .models import *

class TopicAdmin(admin.ModelAdmin):
    pass

admin.site.register(Topic, TopicAdmin)

class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)
