from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat')  # Redirect to the chat view after login
    return render(request, 'login.html')

# Chat View
@login_required
def chat_view(request):
    users = User.objects.exclude(username=request.user.username)  # Exclude the logged-in user
    return render(request, 'chat.html', {'users': users})
#chat_room view

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from chat.models import Message
from django.contrib.auth.models import User

@login_required
def chat_room(request, user_id):
    user_to_chat_with = get_object_or_404(User, id=user_id)
    
    # Handle sending messages
    if request.method == "POST":
        message_content = request.POST.get('message')
        if message_content:
            # Create a new message
            Message.objects.create(sender=request.user, recipient=user_to_chat_with, content=message_content)
            return redirect('chat_room', user_id=user_id)  # Redirect to the same chat room

    # Get all messages between the logged-in user and the selected user
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=user_to_chat_with)) |
        (Q(sender=user_to_chat_with) & Q(recipient=request.user))
    ).order_by('timestamp')

    # Debug print statement to check messages
    print(f"Messages: {messages}")  # This line should be inside the view function

    return render(request, 'chat_room.html', {'user': user_to_chat_with, 'messages': messages})


#chat_room view
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Message, User

@login_required
def chat_room(request, user_id):
    # Get the user you're chatting with
    user_to_chat_with = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        # Process the message sent via the form
        message_content = request.POST.get('message')
        if message_content:
            Message.objects.create(
                sender=request.user,
                recipient=user_to_chat_with,
                content=message_content
            )
            return redirect('chat_room', user_id=user_id)

    # Retrieve messages between the logged-in user and the selected user
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=user_to_chat_with)) |
        (Q(sender=user_to_chat_with) & Q(recipient=request.user))
    ).order_by('timestamp')

    # Render the chat room template
    return render(request, 'chat_room.html', {
        'user': user_to_chat_with,
        'messages': messages
    })
