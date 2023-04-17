from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Lection, Course, Hometask

admin.site.register(Lection)
admin.site.register(Course)
admin.site.register(Hometask)



# ????????
# class ProfileAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = SignUpForm
#     model = Profile
#     list_display = ['email', 'username',]
#
#
# admin.site.register(Profile, ProfileAdmin)