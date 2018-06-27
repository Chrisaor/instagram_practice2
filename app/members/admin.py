from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from members.views import User

admin.site.register(User, UserAdmin)