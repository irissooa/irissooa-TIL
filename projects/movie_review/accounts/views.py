from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods,require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import User
# Create your views here.

def index(request):
    User = get_user_model()
    users = User.objects.all()[::-1]
    context = {
        'users':users,
    }
    return render(request,'accounts/index.html',context)


@require_http_methods(['GET','POST'])
def signup(request):
    #이미 인증된 사용자 전체리뷰페이지로
    if request.user.is_authenticated:
        return redirect('community:review_list')
    #POST일때 -> user정보를 usercreationform에 저장해서 회원가입!
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            #유효성 검사후 맞으면 저장!
            user = form.save()
            #그리고 로그인!
            auth_login(request,user)
            return redirect('community:review_list')
     
    #GET일때는 -> 회원가입폼을 보여줌!
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)


@require_http_methods(['GET','POST'])
def login(request):
    #이미 인증된 사용자 전체리뷰페이지로
    if request.user.is_authenticated:
        return redirect('community:review_list')
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'community:review_list')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('community:review_list')



def profile(request,user_id):
    User = get_user_model()
    person = get_object_or_404(User,username=user_id)
    context = {
        'person':person,
    }
    return render(request,'accounts/profile.html',context)


@require_POST
def follow(request,user_id):
    if request.user.is_authenticated:
        you = get_object_or_404(get_user_model(),pk=user_id)
        me = request.user

        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
            else:
                you.followers.add(me)
        return redirect('accounts:profile',you.username)
    return redirect('accounts:login')