from django.urls import path
from .import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginpage, name='login'),
    path('postpage/<str:pk>/', views.postPage, name="postpage"),
    path('deletecomment/', views.deleteComment, name='delete-comment'),
    
]