from django import forms

from .models import Post, PostTag, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField()

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            tags= [t.name for t in
                                  kwargs['instance'].tag_set.all()]
            initial['tags'] = ", ".join(e for e in tags)
            print(initial['tags'])
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        # instance = forms.ModelForm.save(self, False)
        post = super().save(commit)
        if commit:
            post.save()
            tag_text = self.cleaned_data['tags']
            tag, created = Tag.objects.get_or_create(name=tag_text)
            post_tag = PostTag.objects.create(tag=tag, post=post)
            post_tag.save()
        return post

    class Meta:
        model = Post
        fields = ('title', 'description', 'tags')
        widgets = {
            'tags': forms.TextInput,
        }


