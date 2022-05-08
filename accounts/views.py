from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import UserCreateForm, SingUpForm

from users.models import User

def signup_view(request):
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SingUpForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        # POST 요청 시 데이터 확인 후 회원 생성
        form = SingUpForm(request.POST)

        if form.is_valid():
            #회원가입 처리
            instance = form.save() 
            return redirect('index')           
        else:
            #리다이렉트
            return redirect('accounts:signup')

def login_view(reqeust):
    # GET, POST 분리
    if reqeust.method == 'GET':
        # 로그인 HTML 응답
        return render(reqeust, 'accounts/login.html', {'form': AuthenticationForm()})
    else:
        # 데이터 유효성 검사
        form = AuthenticationForm(reqeust, data=reqeust.POST)
        if form.is_valid():
            # 비즈니스 로직 처리 - 로그인 처리
            login(reqeust, form.user_cache)
            # 응답
            return redirect('index')
        else:
            # 비즈니스 로직 처리 - 로그인 실패
            # 응답
            return render(reqeust, 'accounts/login.html', {'form': form})

        # username = reqeust.POST.get('username')
        # if username == '' or username == None:
        #     pass
        # user = User.objects.get(username=username)
        # if user == None:
        #     pass
        # password = reqeust.POST.get('password')

def logout_view(request):
    #데이터 유효성 검사
    if request.user.is_authenticated:
        #비즈니스 로직 처리 - 로그아웃
        logout(request)
    #응답
    return redirect('index')