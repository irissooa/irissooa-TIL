from django.shortcuts import render,redirect,get_object_or_404
from .models import Review,Comment
from .forms import ReviewForm,CommentForm
from django.views.decorators.http import require_http_methods,require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'community/index.html')

def review_list(request):
    reviews = Review.objects.all()[::-1]
    context ={
        'reviews':reviews,
    }
    return render(request,'community/review_list.html',context)


@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method =='POST':
        form = ReviewForm(request.POST,files=request.FILES)
        if form.is_valid():
            #user인자에다가 request의 user정보를 담는다
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:review_detail',review.pk)
    else:
        form = ReviewForm()
    context = {
        'form':form,
    }
    return render(request,'community/form.html',context)
       

def review_detail(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    comments = review.comment_set.all()[::-1]
    comment_form = CommentForm()
    context = {
        'review':review,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request,'community/review_detail.html',context)


@require_POST
def comments(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.save()
    return redirect('community:review_detail',review.pk)


@require_POST
def like(request,review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review,pk=review_pk)
        if review.like.filter(pk=request.user.pk).exists():
            review.like.remove(request.user)
        else:
            review.like.add(request.user)
        return redirect('community:review_list')
    return redirect('accounts:login')


@require_POST
def like_comment(request,review_pk,comment_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment,pk=comment_pk)
        if comment.like_comment.filter(pk=request.user.pk).exists():
            comment.like_comment.remove(request.user)
        else:
            comment.like_comment.add(request.user)
        return redirect('community:review_detail',review.pk)
    return redirect('accounts:login')