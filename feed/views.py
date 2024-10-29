# views.py
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def feed_view(request):
    if request.method == 'POST':
    
        content = request.POST.get('content')
        if content:
            Post.objects.create(user=request.user, content=content)
            return redirect('feed') 

    posts = Post.objects.all().order_by('-created_at')  
    return render(request, 'feed/feed.html', {'posts': posts}) 
