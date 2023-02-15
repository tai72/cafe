from accounts.models import CustomUser
from django.db import models
from django.dispatch import receiver
from google.cloud import exceptions


class CafeMenu(models.Model):
    """カフェのメニューのモデル"""

    # カスタムユーザーモデルから引っ張ってくる.
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='media/')
    name = models.CharField(verbose_name='商品名', max_length=255, default='商品名')
    price = models.PositiveIntegerField(verbose_name='値段')
    description = models.CharField(verbose_name='説明', max_length=255)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        # 管理画面での表示名を指定。
        verbose_name_plural = 'Cafe_App'
    
    # 管理画面でレコードを判明できるように表示されるものを設定.
    def __str__(self):
        return self.name
    
@receiver(models.signals.post_delete, sender=CafeMenu)
def auto_delete_image(sender, instance, **kwargs):
    print('写真削除します')
    file = instance.photo
    try:
        file.storage.delete(name=file.name)
        print('削除しました')
    except exceptions.NotFound as e:
        print(e)
