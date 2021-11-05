from django.contrib import admin

# 관리자 페이지에 모델 등록
from .models import Bookmark


# Register your models here.

# 관리자 페이지에 모델 등록
admin.site.register(Bookmark)

