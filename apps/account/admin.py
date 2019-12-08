from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Register your models here.
#admin.site.register(Profile)


class ProfileInline(admin.StackedInline):
    model = Profile


class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'photo', 'date_of_birth', 'hide_age', 'city',
                    'marriage_status')


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline,]


admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
