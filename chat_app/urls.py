# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),  # Define your index view here
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('chat/', views.chat_view, name='chat'),
    path('chat/<int:user_id>/', views.chat_room, name='chat_room'),
]

