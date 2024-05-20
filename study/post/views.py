from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Post, PostImages

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['title', 'content']


# Create your views here.

def write(request):
    if request.method == "POST":
        form=PostForm(request.POST)
        post=form.save()
        images=request.FILES.getlist('images')
        for img in images:
            PostImages.objects.create(post=post, image=img)
        return redirect('main')
    else:
        form=PostForm()
        return render(request, 'write.html', {'form':form})
    
def detail(request, id):
    post=get_object_or_404(Post, pk=id)
    images=PostImages.objects.filter(post=post)
    return render(request, 'detail.html', {'post':post, 'images':images})