from django.contrib import admin

from .models import CustomUser

# 管理サイトにカスタムユーザーモデルを登録する
admin.site.register(CustomUser)
