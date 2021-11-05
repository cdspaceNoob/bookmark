from django.db import models

# Create your models here.
# 여기는 bookmark기능(bookmark앱)에서 실행하는 정보들이 저장되는 데이터베이스를 관리한다

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    def __str__(self):
        # 객체를 출력할 때 나타낼 값
        return "이름 : "+self.site_name + ", 주소 : "+self.url
