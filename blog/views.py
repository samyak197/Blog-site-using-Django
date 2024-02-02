from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.contrib.auth.models import User
from .models import Post
from django.views import generic
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "latest_blog_list"

    def get_queryset(self):
        return Post.objects.order_by("-pb_date")[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/details.html"
    context_object_name = "blog"


class CreateView(generic.CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["blog_title", "blog_content", "author", "category", "tag"]
    success_url = reverse_lazy("blog:index")


class UpdateView(generic.UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    context_object_name = "blog"
    fields = ["blog_title", "blog_content", "author", "category", "tag"]
    success_url = reverse_lazy("blog:index")


class DeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/confirm_delete.html"
    context_object_name = "blog"
    success_url = reverse_lazy("blog:index")
