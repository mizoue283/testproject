from django.db import models
from django.contrib.auth.models import User as DjangoUser
from .forms import RegisterForm, LoginForm
from django.utils import timezone

'''
DjangoのデフォルトUserモデルを継承して、インスタンスメソッドを追加している
'''


class User(DjangoUser):
    '''
    新規にtableを作成せずに継承したmodelの拡張のみを行いたいので、
    MetaクラスのproxyをTrueにしている。
    '''


    class Meta:
        proxy = True

    '''
    Userインスタンスがフォローしているuserを返す関数
    '''

    def get_followers(self):
        relations = Relationship.objects.filter(follow=self)
        return [relation.follower for relation in relations]


'''
フォローしている人と、フォローされている人をつなぐ中間テーブル
'''


class Relationship(models.Model):
    follow = models.ForeignKey(User, related_name='follows')
    follower = models.ForeignKey(User, related_name='followers')


class Tweet(models.Model):
    userprofile = models.ForeignKey(User)
    tweets = models.TextField(max_length=120)
    created_date = models.DateTimeField(default=timezone.now)
    active_date = models.IntegerField()

    def __str__(self):
        return  str(self.userprofile)
