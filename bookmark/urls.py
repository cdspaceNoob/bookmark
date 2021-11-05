# 이 파일은 http://127.0.0.1:8000/bookmark/ 이하의 부분을 가지고
# 어떤 뷰를 연결할지를 작성해놓은 서브 urls파일임

from django.urls import path
from .views import BookmarkListView, BookmarkCreateView

# 북마크 확인 기능 뷰에 URL을 연결하기 위한 임포트
from .views import *

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
]