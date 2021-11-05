# 이 파일은 http://127.0.0.1:8000/bookmark/ 이하의 부분을 가지고
# 어떤 뷰를 연결할지를 작성해놓은 서브 urls파일임

from django.urls import path
from .views import BookmarkListView, BookmarkCreateView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
]