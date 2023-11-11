from django.urls import path
from . import views

urlpatterns = [
 # Home page.
 path('', views.index, name='index'),
 path('about/', views.about, name='about'),
 path('contact/', views.contact, name='contact'),
 path('services/', views.services, name='services'),
#  path('blog/',views.handleBlog,name='handleBlog'),
 path('blog/',views.bloghome, name='bloghome'),
 path("blog/<str:slug>",views.blogposts, name ="blogPost"),
 path('search',views.search,name='search'),

#  login/signup/loguot
 path('login/',views.handlelogin,name='handlelogin'),
 path('logout/',views.handlelogout,name='handlelogout'),
 path('signup/',views.handlesignup,name='handlesignup'),
#  search/

]