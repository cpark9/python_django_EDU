from django.db import models
from django.conf import settings 

# Create your models here.
class Article(models.Model): # 상속
    # id는 자동으로 만들어진다.
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return str(f'No : {self.id}, 제목 : {self.title}')
  