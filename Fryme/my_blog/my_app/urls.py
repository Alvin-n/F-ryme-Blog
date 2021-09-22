from django.urls import path 
from .views import home_view, about_view, contact_view, login_view, logout_view, post_create_view,post_view, register_view


urlpatterns = [
path("", home_view, name = 'home_page'),
path("About/", about_view, name= 'about_page'),
path("Contact/", contact_view, name= 'contact_page'),
path("Post/<int:post_id>/", post_view, name= 'post_page'),
path("Post_Create/", post_create_view, name= 'post_create_page'),
path("Register/", register_view, name= 'register_page'),
path("Login/", login_view, name= 'login_page'),
path('logout/', logout_view, name='logout_page'),
]