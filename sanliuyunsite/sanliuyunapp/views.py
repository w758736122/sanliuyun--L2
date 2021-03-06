from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponse,StreamingHttpResponse
from sanliuyunapp.form import registerForm,loginForm, ArticleForm,uploadArtForm
from sanliuyunapp.models import Person, Article


def indexView(request):
    context = {}
    return render(request,'index.html',context)

def uploadView(request):
    context = {}
    if request.method == 'GET':
        form = uploadArtForm
    if request.method == 'POST':
        form = uploadArtForm(request.POST,request.FILES)
        if form.is_valid():
            user_id = request.user.user_profile.id
            headline = form.cleaned_data['headline']
            upload_art = request.FILES['uploadArt']
            art = Article(headline = headline,local_article=upload_art)
            art.save()
            art.author.add(user_id)
            art.save()
            return redirect(to='desktop')
    context['form'] = form
    return render(request,'upload.html',context)

def downloadArtView(request,art_name):
    context = {}
    user_id = request.user.id
    headline = art_name
    art = Article.objects.get(headline = art_name)
    content = art.text
    target = "D:\{}.doc".format(headline)
    with open(target,'w') as fs:
        for chunk in content:
            fs.write(chunk)
        fs.close()
        return HttpResponse('已经导出到D盘根目录')
    return render(request,'desktop.html',context)



@login_required(redirect_field_name='login',login_url='login')
def desktopView(request):
    context = {}
    user_id = request.user.id
    art = Article.objects.filter(author = user_id).order_by('-save_time')
    page_robot = Paginator(art,15)
    page_num = request.GET.get('page')
    if page_num:
        page = int(page_num)
    else:
        page = 1#不加index 跳转进来会报错
    try:
        art = page_robot.page(page_num)
    except EmptyPage:
        art = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        art = page_robot.page(1)
    if page == int(page_robot.num_pages):
        page_range = page_robot.page_range[page-5:page_robot.num_pages]
    elif page == int(page_robot.num_pages)-1:
        page_range = page_robot.page_range[page-4:page_robot.num_pages+1]
    elif page <= 2:
        page_range = page_robot.page_range[0:5-page+page]
    else:
        page_range = page_robot.page_range[page-3 :page+2]
    context['art'] =art
    context['page_range'] =page_range

    return render(request,'desktop.html',context)

def loginView(request):
    context={}
    if request.method == 'GET':
        form = loginForm
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            inputName = form.cleaned_data['inputName']
            password = form.cleaned_data['password']
            try:
                user = authenticate(username =inputName,password = password)
                if user:
                    login(request,user)
                    return redirect(to = 'index')
                else:
                    person = Person.objects.get(email_address = inputName)
                    inputName = person.nickname
                    user = authenticate(username =inputName,password = password)
                    if user:
                        login(request,user)
                        return redirect(to = 'index')
                    else:
                        return HttpResponse('用户名/密码错误')
            except Person.DoesNotExist:
                return HttpResponse('用户名不存在')
            return redirect(to = 'index')
    context['form']= form
    return render(request,'login.html',context)

def registerView(request):
    context={}
    if request.method == 'GET':
        form = registerForm
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            email_address = form.cleaned_data['email_address']
            if nickname ==email_address:
                return HttpResponse('昵称和邮箱地址不能一样哦~')
            try:
                nickname_judge = Person.objects.get(nickname = nickname )
                if nickname_judge:
                    return HttpResponse('用户名重复了~')
            except:
                email_judge= Person.objects.get(email_address = email_address )
                if email_judge:
                    return HttpResponse('邮箱重复了~')
            ##判断是否邮箱已经存在
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 == password2:
                    new_Person = User.objects.create_user(username =nickname,password = password2)
                    new_Person.save()
                    person = Person(belong_to= new_Person,nickname=nickname,email_address= email_address)
                    person.save()
                    user = authenticate(username =nickname,password = password2)
                    if user:
                        login(request,user)
                        return redirect(to = 'index')
                else:
                    return HttpResponse('2次密码不同，请重新输入')
    context['form']= form
    return render(request,'register.html',context)

def deleteArtView(request,art_name):
    context = {}
    try:
        art = Article.objects.get(id = art_name)
        if request.method == 'GET':
            pass
        if request.method == 'POST':
            art.delete()
            return redirect('delResult')

    except:
        return HttpResponse('页面已经删除了~')
    return render(request,'deleteArt.html',context)

def deleteResultView(request):
    context = {}
    return render(request,'deleteResult.html',context)


def editorView(request):

    context = {}
    if request.method == 'GET':
        form = ArticleForm
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            headline = form.cleaned_data['headline']
            content = form.cleaned_data['content']
            a = Article(headline=headline, text=content)
            a.save()


    # article = Article.objects.get()
    context['form'] = form
    # context['article'] = article
    editor_page = render(request, 'editoring.html', context)

    return editor_page
