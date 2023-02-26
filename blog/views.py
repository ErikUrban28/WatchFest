from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .models import CustomUser
from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, "blog/home.html")


def about(request):
    return render(request, "blog/about.html")


def articles(request):
    data = {
        'articles': Article.objects.all()
    }
    return render(request, "blog/articles.html", data)


def register(request):
    form = RegisterForm(data=request.POST or None)
    context = {'form': form}
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('blog-index')
    return render(request, "blog/register.html", context)


def login_user(request):
    form = LoginForm(data=request.POST or None)
    context = {'form': form}
    if form.is_valid():
        user = form.get_user()
        if user:
            login(request, user)
            return redirect('blog-authenticated')
    return render(request, "blog/login.html", context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('blog-index')


@login_required
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('blog-articles')


@login_required
def user_profile(request):
    return render(request, "blog/editUser.html")


@login_required
def edit_profile(request):
    if request.POST:
        user = get_object_or_404(CustomUser, pk=request.user.id)
        user.login = request.POST['login']
        user.password = make_password(request.POST['password'])
        user.email = request.POST['email']
        user.save()
        login(request, user)
        return redirect('blog-index')
    return render(request, "blog/editUser.html")


@login_required
def article_form(request, id=None):
    data = {}
    if id:
        article = get_object_or_404(Article, id=id)
        data = {'article': article}
    else:
        article = Article(author_id=request.user.id)
    if request.POST:
        article.title = request.POST['title']
        article.text = request.POST['text']
        article.img = request.POST['img']
        article.save()
        return redirect('blog-articles')
    return render(request, "blog/articleForm.html", data)


@login_required
def authenticated(request):
    return render(request, "blog/authenticated.html")
