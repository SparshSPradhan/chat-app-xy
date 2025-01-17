
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from chat.models import Message


@login_required
def chat_view(request):
    # Get all users except the current user
    users = User.objects.exclude(id=request.user.id)
    
    return render(request, 'chat.html', {'users': users})



#chat_room view


# @login_required
# def chat_room(request, user_id):
#     user_to_chat_with = get_object_or_404(User, id=user_id)
    
#     # Handle sending messages
#     if request.method == "POST":
#         message_content = request.POST.get('message')
#         if message_content:
#             # Create a new message
#             Message.objects.create(sender=request.user, recipient=user_to_chat_with, content=message_content)
#             return redirect('chat_room', user_id=user_id)  # Redirect to the same chat room

#     # Get all messages between the logged-in user and the selected user
#     messages = Message.objects.filter(
#         (Q(sender=request.user) & Q(recipient=user_to_chat_with)) |
#         (Q(sender=user_to_chat_with) & Q(recipient=request.user))
#     ).order_by('timestamp')

#     # Debug print statement to check messages
#     print(f"Messages: {messages}")  # This line should be inside the view function

#     return render(request, 'chat_room.html', {'user': user_to_chat_with, 'messages': messages})



@login_required
def chat_room(request, user_id):
    try:
        user_to_chat_with = get_object_or_404(User, id=user_id)
        print(f"Chatting with user: {user_to_chat_with.username}")

        if request.method == "POST":
            message_content = request.POST.get('message')
            if message_content:
                Message.objects.create(sender=request.user, recipient=user_to_chat_with, content=message_content)
                return redirect('chat_room', user_id=user_id)

        messages = Message.objects.filter(
            (Q(sender=request.user) & Q(recipient=user_to_chat_with)) |
            (Q(sender=user_to_chat_with) & Q(recipient=request.user))
        ).order_by('timestamp')

        print(f"Messages: {messages}")
        return render(request, 'chat_room.html', {'user': user_to_chat_with, 'messages': messages})
    except Exception as e:
        print(f"Error in chat_room view: {e}")
        raise e





# User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            user = authenticate(username=username, password=form.cleaned_data["password1"])
            if user is not None:
                login(request, user)
                return redirect('chat')  # Redirect to the chat view after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login View


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print(f"User {user.username} logged in")  # Add a print statement to confirm login
                return redirect('chat')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})
