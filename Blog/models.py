from django.db import models


class Tag(models.Model):
    '''
    標籤，多對多分類，多選
    '''
    title = models.CharField('標籤', max_length=30, unique=True)
    shortUrl = models.CharField('短Url', max_length=150, unique=True, null=False, blank=False, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Category(models.Model):
    '''
    分類，一對多，單選
    '''
    title = models.CharField('分類', max_length=30, unique=True)
    shortUrl = models.CharField("短URL", max_length=150, unique=True, null=False, blank=False, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Blog(models.Model):
    title = models.CharField("標題", max_length=150, unique=True, null=False, blank=False)
    createTime = models.DateTimeField("創建時間", auto_now_add=True, auto_now=False)
    updateTime = models.DateTimeField("修改時間", auto_now_add=False, auto_now=True)
    body = models.TextField("內容")
    accessCount = models.IntegerField("瀏覽量", default=1, editable=False)
    category = models.ForeignKey('Category', verbose_name="分類集合", related_name='category')
    shortUrl = models.CharField("短URL", max_length=150, unique=True, null=False, blank=False, editable=False)
    tags = models.ManyToManyField('Tag', verbose_name="標籤集合", null=True, editable=False)
    tags.help_text = '標籤集合'

    def __str__(self):
        return self.title


