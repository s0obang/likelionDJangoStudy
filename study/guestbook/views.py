from django.shortcuts import render, redirect
from django import forms
from .models import GuestBook

class WriteForm(forms.ModelForm):
    class Meta:
        model=GuestBook
        fields = ['name', 'password', 'content']
# Create your views here.
def write(request):
    if request.method=='POST':
        form=WriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/guestbook')
        return render(request, 'writeguestbook.html')
    else:
        form=WriteForm()
        return render(request, 'writeguestbook.html', {'form': form })



def guestbook(request):
    books=GuestBook.objects.all().order_by('-write_time')
    
    return render(request, 'guestbook.html',{'books':books})

def deleteform(request, id=0):
    return render(request, 'deleteform.html', {'id':id})

def delete(request):
    id = request.POST['idval']
    password = request.POST['password']

    guestbook = GuestBook.objects.filter(id=id)
    if guestbook[0].password == password:
        guestbook.delete()

    return redirect('/guestbook')