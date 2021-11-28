from django.urls import path 
from .views import LoginView, RegisterView, home_view, about_view, contact_view, logout_view, post_create_view,post_view


urlpatterns = [
path("", home_view, name = 'home_page'),
path("about/", about_view, name= 'about_page'),
path("contact/", contact_view, name= 'contact_page'),
path("post/<int:post_id>/", post_view, name= 'post_page'),
path("post_create/", post_create_view, name= 'post_create_page'),
path('login/', LoginView.as_view(), name='login_page'),
path('register/', RegisterView.as_view(), name='register_page'),
path('logout/', logout_view, name='logout_page'),
]