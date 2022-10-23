from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField('商品名稱', max_length=50)
    image = models.FileField(upload_to='image/', blank=True)
    # upload_to 指定上传文件位置
    # 这里指定存放在 img/ 目录下
    description = models.TextField(
        '商品描述', max_length=500, null=True, blank=True)
    price = models.PositiveIntegerField('商品價格', default=0)
    created = models.DateTimeField('建立日期', auto_now_add=True)
    modified = models.DateTimeField('修改日期', auto_now_add=True)

    def __str__(self):
        return f'{self.name}---{self.price}元'
