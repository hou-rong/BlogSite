from django.db import models


class Blog(models.Model):
    title = models.CharField("標題", max_length=150, unique=True, null=False, blank=False)
    createTime = models.DateTimeField("創建時間", auto_now_add=True, auto_now=False)
    updateTime = models.DateTimeField("修改時間", auto_now_add=False, auto_now=True)
    body = models.TextField("內容")
    shortUrl = models.CharField("短URL", max_length=150, unique=True, null=False, blank=False)
    # todo tags have not set

    def __str__(self):
        return self.title
