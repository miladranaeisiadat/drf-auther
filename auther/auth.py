import json

from django.conf import settings
from redisary import Redisary
from rest_framework.exceptions import APIException
from rest_framework.request import Request

from auther.models import User
from auther.utils import generate_token, check_password

tokens = Redisary(db=settings.AUTHER['REDIS_DB'])


def authenticate(request: Request) -> User:
    username = request.data['username']
    password = request.data['password']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise APIException('Username not found')

    if check_password(password, user.password):
        return user

    raise APIException('Wrong password')


def login(user: User) -> str:
    token = generate_token()

    payload = {
        'id': user.id,
        'name': user.name,
        'username': user.username,
        'avatar_pic': user.avatar_pic,
        'domain_id': user.domain.id if user.domain else None,
        'role': user.role.name
    }
    tokens[token] = json.dumps(payload)

    return token
