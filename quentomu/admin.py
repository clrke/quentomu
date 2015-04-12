from django.contrib import admin
from .models import *

class TopicAdmin(admin.ModelAdmin):
    pass

admin.site.register(Topic, TopicAdmin)

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)

class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)

class AddressAdmin(admin.ModelAdmin):
    pass

admin.site.register(Address, AddressAdmin)
