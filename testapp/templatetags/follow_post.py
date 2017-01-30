from django.shortcuts import render, get_object_or_404
from testapp.models import User, Relationship, Tweet
# coding: utf-8
from django import template

register = template.Library()
"""
 カスタムテンプレートフィルター
"""


# register.filterデコレータ
# register.filter('is_any_data_exists', is_any_data_exists')でも可
@register.filter(name='follow')
def user_follow(user_id, id):
    users = get_object_or_404(User, id=id)
    user = get_object_or_404(User, id=user_id)
    follow_user = Relationship.objects.create(follow=user, follower=users)
    return follow_user


@register.filter(name='unfollow')
def user_unfollow(user_id, id):
    users = get_object_or_404(User, id=id)
    user = get_object_or_404(User, id=user_id)
    unfollow_user = Relationship.objects.filter(follow=user, follower=users).delete()
    return unfollow_user
