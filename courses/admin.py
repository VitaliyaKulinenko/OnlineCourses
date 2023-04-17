from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Lection, Course

admin.site.register(Lection)
admin.site.register(Course)


# ????????
# class ProfileAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = SignUpForm
#     model = Profile
#     list_display = ['email', 'username',]
#
#
# admin.site.register(Profile, ProfileAdmin)