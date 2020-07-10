from django.contrib import admin  
from django.urls import path  
from .views import AuthorEdit, AuthorList, BookList, author_create_many, books_authors_create_many,FriendEdit, FriendList
from p_library.views import index, logout, login ,  RegisterView, CreateUserProfile
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy  
from allauth.account.views import login, logout

app_name = 'p_library'  
"""urlpatterns = [  
  path('author/create', AuthorEdit.as_view(), name='author_create'),  
  path('authors', AuthorList.as_view(), name='author_list'),
  path('author/create_many', author_create_many, name='author_create_many'),
  path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),  
]"""

"""urlpatterns = [  
    path('', index, name='index'),  
    path('logout/', logout, name='logout'), 
    #за маршрут logout/ отвечал этот стандартный обработчик
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('login/', login, name='login'),
    #за маршрут login/ отвечал этот стандартный обработчик
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    #регистрация с редериктом на редактирование профиля
    path('register/', RegisterView.as_view(template_name='register.html', success_url=reverse_lazy('p_library:profile-create')  
    ), name='register'),
    #редактирование профиля
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),     
]"""
"""path('author/create', AuthorEdit.as_view(), name='author_create'),
        path('authors', AuthorList.as_view(), name='author_list'),
        path('books', BookList.as_view(), name='book_list'),
        path('friends/create', FriendEdit.as_view(), name='friend_create'),
        path('friends', FriendList.as_view(), name='friend_list'),
        path('author/create_many', author_create_many, name='author_create_many'),
        path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),"""

urlpatterns = [  
    path('', index, name='index'),  
    path('login/', login, name='login'),  
    path('logout/', logout, name='logout'),
    path('register/', RegisterView.as_view(template_name='register.html', success_url=reverse_lazy('p_library:profile-create')  
    ), name='register'),
    #редактирование профиля
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
    #path('accounts/', include('allauth.urls')),     
]