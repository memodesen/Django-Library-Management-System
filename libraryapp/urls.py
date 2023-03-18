from django.urls import path
from . import views

# http://127.0.0.1:8000         => index
# http://127.0.0.1:8000/details => details
# http://127.0.0.1:8000/list    => list

urlpatterns = [
    path('', views.index,name="index"),
    path('index', views.index,name="index"),
    path('admin-login/', views.admin_login, name='admiin'),
    path('register', views.register, name='register'),
    path('loginn', views.loginn, name='loginn'),
    path('user', views.user, name='user'),
    path('books', views.books, name='books'),
    path('issue', views.issue, name='issue'),
    path('logout/', views.logout_view, name='logout'),
]