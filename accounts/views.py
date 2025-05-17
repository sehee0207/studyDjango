from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from app.forms import PostForm
from app.models import Post


@login_required
def index(request: HttpRequest) -> HttpResponse:

    qs = Post.objects.all()
    return render(
        request,
        "app/index.html",
        {
            "post_list": qs,
        },
    )
