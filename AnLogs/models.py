from django.db import models

# Create your models here.

class log(models.Model):
    id = models.AutoField(primary_key=True)
    clinetIp=models.GenericIPAddressField(verbose_name="IP地址")
    facility=models.CharField(verbose_name="模块",max_length=128)
    serverity=models.CharField(verbose_name="等级",max_length=128)
    header=models.TimeField(verbose_name="时间")
    msg=models.TextField(verbose_name="消息内容")

    class Meta:
        verbose_name = "日志信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.clinetIp
