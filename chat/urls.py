# from django.urls import path
# from . import views

# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('chat/', views.chat_view, name='chat'),
# ]
from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat_app.urls')),  # This will include chat app URLs

]
