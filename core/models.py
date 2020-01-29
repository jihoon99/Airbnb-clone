from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):

    """ Time Stamped Model """


    created = models.DateTimeField(auto_now_add=True) # 장고가 model을 만들면 현제시간 날짜를 넣어줌.
    updated = models.DateTimeField(auto_now=True) # 내가 model을 저장할때마다 새로운 날짜를 줌.


    class Meta:
        abstract = True