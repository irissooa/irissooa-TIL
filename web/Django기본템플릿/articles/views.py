from django.shortcuts import render,redirect,get_object_or_404
from .models import Article,Comment
from .forms import ArticleForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1]
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html',context)


@login_required
def create(request):
    if request.method =='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail',article.pk)
    else:
        form =ArticleForm()
    context = {
        'form':form,
    }
    return render(request,'articles/create.html',context)


@login_required
def detail(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    comments = article.comment_set.all()[::-1]
    comment_form = CommentForm()
    context = {
        'article':article,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request,'articles/detail.html',context)


@login_required
def update(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST,instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail',article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form':form,
        }
        return render(request,'articles/update.html',context)
    return redirect('articles:index')

@require_POST
def delete(request,article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article,pk=article_pk)
        if request.user == article.user:
            article.delete()
    return redirect('articles:index')


@require_POST
def comments_create(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()
    context = {
        'comment_form' :comment_form,
        'article':article,
    }
    return redirect('articles:detail',article.pk)
    

@require_POST
def comment_delete(request,article_pk,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail',article_pk)


@require_POST
def like(request,article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article,pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')