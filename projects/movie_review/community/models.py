from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_reviews')
    # image = ProcessedImageField(
    #     blank=True, 
    #     #사용자가 올린 이미지 가공을 해서 원본그대로가 아니라 썸네일처럼 잘라서 올림
    #     processors=[Thumbnail(200,300)],
    #     format='JPEG',
    #     options={'quality':90},
    #     upload_to='%Y/%m/%d',
    # )
    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=100)
    review = models.ForeignKey(Review,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    like_comment = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_comments')

    def __str__(self):
        return self.content