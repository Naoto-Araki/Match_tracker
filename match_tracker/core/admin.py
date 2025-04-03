from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, GameType, Match

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # 一覧ページに表示する項目
    list_display = ['username', 'email', 'nickname', 'is_staff']

    # ユーザー詳細ページ（編集画面）に表示する項目
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nickname',)}),
    )

    # ユーザー作成画面（add user）に表示する項目
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nickname',)}),
    )

# 登録
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(GameType)
admin.site.register(Match)
