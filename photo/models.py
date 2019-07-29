from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

class Photo(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_photos')
    photo=models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png') #사진 저장할 위치 설정
    text=models.TextField() #텍스트

    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True) #날짜 자동 생성/수정

    class Meta:
        ordering=['-updated'] #객체들을 어떤 기준으로 정렬할 것인지 : 수정시간의 내림차순
    
    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S") #글 제목에 작성자이름+날짜 표기

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)]) #객체의 상세페이지 주소 반환 메서드