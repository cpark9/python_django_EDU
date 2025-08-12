from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# UserAdmin 은 user관리에서 만 사용 가능
admin.site.register(User, UserAdmin)