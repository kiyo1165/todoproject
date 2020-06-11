from django.db import models


PRIORITY = (('danger','high'),('info','normal'),('success','low')) #選択リストはタプル型で指定。
# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100) #タイトルなどの短い文字列
    memo = models.TextField() #本文など長い文字列
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY #プルダウンの選択はchoicesを使用
    )

    duedate = models.DateField() #日付データを入力するフィールド
    def __str__(self): #管理画面作成されたオブジェクトのタイトルをindexで表示される
        return self.title