from django.urls import path
from .views import TagDetailView, TagListView

app_name = 'tag'

urlpatterns = [
    path("", TagListView.as_view(), name='tag-list'),
    path('<slug:slug>', TagDetailView.as_view(), name='tag-detail'),
]
