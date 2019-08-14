from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DeleteView, ListView, TemplateView, CreateView, DetailView, View, UpdateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Comment, Category, Post, PostTag, Tag

import re


class PostCreateView(TemplateView):
    template_name = "post/post_create.html"


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(category=None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_list'] = Category.objects.all()
        context['form'] = PostForm(self.request.GET)
        return context


class DetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'


class PostComment(View):
    login_required = True

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            comment = Comment()
            comment.text = request.POST['text']
            comment.user = request.user
            comment.post = Post.objects.get(pk=self.kwargs.get('pk'))
            comment.publish()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect('account:login')


class PostLike(View):
    login_required = True

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            post = Post.objects.get(pk=self.kwargs.get('pk'))
            post.like = post.like + 1
            post.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect('account:login')


class CommentLike(View):
    login_required = True

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            comment = Comment.objects.get(pk=self.kwargs.get('comment_pk'))
            comment.like = comment.like + 1
            comment.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect('account:login')


class PostCreateView(CreateView):
    login_required = True
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post:post-list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()

        tag_text = form.cleaned_data['tags']
        tag, created = Tag.objects.get_or_create(name=tag_text)
        post_tag = PostTag.objects.create(tag=tag, post=obj)
        post_tag.save()

        return redirect('post:post-list')


class PostUpdate(UpdateView):
    login_required = True
    model = Post
    form_class = PostForm
    # fields = ['title', 'description',]

    def form_valid(self, form):
        obj = form.save(commit=False)
        if self.request.user == obj.user:
            obj.save()

            old_tags = obj.tag_set.all()
            tag_text = form.cleaned_data['tags']
            # tag_list = tag_text.split()
            tag_list = re.split(r'[, ]', tag_text)
            old_tags_list = list()

            for old_tag in old_tags:
                old_tag_name = old_tag.name
                if old_tag_name not in tag_list:
                    old_post_tag = PostTag.objects.filter(tag=old_tag, post=obj)
                    if old_post_tag:
                        old_post_tag.first().delete()
                else:
                    old_tags_list.append(old_tag_name)

            for tag_name in tag_list:
                if tag_name and tag_name.strip():
                    if tag_name not in old_tags_list:
                        tag, created = Tag.objects.get_or_create(name=tag_name)
                        post_tag, created = PostTag.objects.get_or_create(tag=tag, post=obj)
                        if created:
                            post_tag.save()

            return redirect('post:post-list')
        else:
            return redirect('account:login')


class PostDelete(DeleteView):
    login_required = True
    model = Post
    success_url = reverse_lazy('post:post-list')

    def delete(self, *args, **kwargs):
        if self.request.user is self.model.user:
            raise Exception(self.model.user)
        return super(PostDelete, self).delete(*args, **kwargs)





