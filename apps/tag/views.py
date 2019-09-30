from django.shortcuts import render
from django.views.generic import DetailView, ListView
from post.models import Tag


class TagListView(ListView):
    model = Tag
    template_name = 'tag/tag_list.html'


class TagDetailView(DetailView):
    model = Tag
    template_name = 'post/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = context['tag'].posts.all()
        context['object_list'] = posts
        return context