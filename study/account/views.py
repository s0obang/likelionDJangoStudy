from django.shortcuts import render, redirect
from .forms import SignUpForm, MyPageForm
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib import messages
from .models import CustomUser, MyPage

# Create your views here.
def signUp(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #성공하면 home으로 바로 보냄
            return render(request, 'main.html')
        return render(request, 'signup.html', {'form': form })
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form } )

def login(request):
    if request.method=='POST':
        id=request.POST.get('id')
        password=request.POST.get('password')
        user=auth.authenticate(request, id = id, password = password)
        #print(user)
        #기본은 id가 아니고 username인데 CustomUser에서 USERNAME_FIELD='id'로 설정해서 일케 해야해여 backends.py에서 약간 바꿨어여
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main')

def main(request):
    return render(request,'main.html')

def mypage(request):
    user = request.user
    mypage_info = MyPage.objects.filter(user=user).first()
    if mypage_info:
        #값 존재할때
        introduction_message = "소개를 추가해보세요" if not mypage_info.introduction else None
        hobby_message = "취미를 추가해보세요" if not mypage_info.hobby else None
        profile_image_message = "이미지를 추가해보세요" if not mypage_info.profile_image else None
        potpolio_message = "포트폴리오 링크를 걸어보세요" if not mypage_info.potpolio else None
    else:
        #존재 안할때
        introduction_message = "소개를 추가해보세요" 
        hobby_message = "취미를 추가해보세요"
        profile_image_message = "이미지를 추가해보세요"
        potpolio_message = "포트폴리오 링크를 걸어보세요"

    return render(request, 'mypage.html', {'mypage_info': mypage_info, 'introduction_message': introduction_message, 'hobby_message': hobby_message, 'profile_image_message': profile_image_message, 'potpolio_message': potpolio_message})

def mypageUpdate(request):
    user = request.user
    mypage_info = MyPage.objects.filter(user=user).first()
    if request.method == 'POST':
        form = MyPageForm(request.POST, request.FILES, instance=mypage_info)
        if form.is_valid():
            form.save()
            return redirect('account:mypage')
    else:
        form = MyPageForm(instance=mypage_info)
    
    return render(request, 'mypage_update.html', {'form': form})


# Create your views here.
