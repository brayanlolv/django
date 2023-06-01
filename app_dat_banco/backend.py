from typing import Any, Optional
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import Q
from django.http.request import HttpRequest


class Login(BaseBackend):

    def authenticate(self, request: Http Request, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        return super().authenticate(request, username, password, **kwargs)