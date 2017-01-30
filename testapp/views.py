from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from blog.models import Post  # 外部APP（blog）からモデルを取ってきている
from .forms import RegisterForm, LoginForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import User, Relationship, Tweet


# class TopPageView(generic.TemplateView):
#    template_name = "testapp/index_info_first.html"

# トップページ(共通)
def post_lists(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date').all()[:3]
    tweets = Tweet.objects.filter(created_date__lte=timezone.now()).order_by('-created_date').all()[:5]

    return render(request, 'testapp/index.html', {'posts': posts, 'tweets': tweets})


def tweet_lists(request):
    tweets = Tweet.objects.filter(created_date__lte=timezone.now()).order_by('-created_date').all()[:5]
    return render(request, 'testapp/index.html', {'tweets': tweets})


class CreateUserView(generic.CreateView):
    template_name = 'testapp/create.html'
    form_class = RegisterForm
    success_url = reverse_lazy('testapp:index')


# ユーザーページ(個々)
@login_required
def user_detail(request, id):
    users = get_object_or_404(User, id=id)
    tweets = Tweet.objects.filter(userprofile_id=id).order_by('-created_date').all()[:5]
    follows_number = len(Relationship.objects.filter(follow=users))
    followers_number = len(Relationship.objects.filter(follower=users))

    return render(request, 'testapp/info.html', {'users': users,
                                                 'tweets': tweets,
                                                 'follows_number': follows_number,
                                                 'followers_number': followers_number,
                                                 #      'follow_user':follow_user,
                                                 'id': id})

@login_required
def user_follow(request,user_id, id):
    users = get_object_or_404(User, id=id)
    user = get_object_or_404(User, id=user_id)
    follow_user = Relationship.objects.create(follow=user, follower=users)
    return follow_user

@login_required
def user_unfollow(request,user_id, id):
    users = get_object_or_404(User, id=id)
    user = get_object_or_404(User, id=user_id)
    unfollow_user = Relationship.objects.filter(follow=user, follower=users).delete()
    return unfollow_user
# ユーザーページ(設定ページ)
@login_required
def Mypage_home(request):
    return render(request, 'testapp/info.html', )


# class MyPageView(LoginRequiredMixin, generic.TemplateView):
#   template_name = "testapp/info.html"



def login(request):
    context = {
        'template_name': 'testapp/login.html',
        'authentication_form': LoginForm

    }
    return auth_views.login(request, **context)


def logout(request):
    context = {
        'template_name': 'testapp/logout.html',
    }
    return auth_views.logout(request, **context)
