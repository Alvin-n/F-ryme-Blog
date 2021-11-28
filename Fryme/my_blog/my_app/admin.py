from django.contrib import admin
from .models import CustomUser, NavbarModel,AboutModel, ContactModel, Footer, NavbarModel, PostImageModel, PostModel, Settings



# Register your models here.
admin.site.register(NavbarModel)
admin.site.register(Settings)
admin.site.register(Footer)
admin.site.register(PostModel)
admin.site.register(AboutModel)
admin.site.register(ContactModel)
admin.site.register(PostImageModel)
admin.site.register(CustomUser)
