from django.shortcuts import render,redirect,reverse
from login import models
# Create your views here.

def log_in(request):
    ''' user log_in '''
    msg=""
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=models.UserInfo.objects.filter(username=username,password=password)
        if user:
            request.session['is_login']=True
            request.session['username']=username
            return redirect(reverse('index'))
        else:
            msg='用户名或密码错误'

    return render(request, 'login.html', {'msg': msg})


def log_out(request):
    request.session.clear()
    return redirect(reverse('log_in'))



def auth(func):
    ''' auth system '''
    def inner(request,*args,**kwargs):
        is_login = request.session['is_login']
        if is_login:
            return func(request,*args,**kwargs)
        else:
            return redirect(reverse('log_in'))
    return inner

@auth
def index(request):
    ''' home page'''
    username = request.session['username']
    cookie_info = request.COOKIES
    session_info = request.session
    print('cookie:{cookie}   session:{session}'.format(cookie=cookie_info, session=session_info))
    return render(request, 'index.html', locals())

