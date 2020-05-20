from django.db import models
import uuid
import django.utils.timezone as timezone
# Create your models here.

class Application(models.Model):
    id = models.AutoField(primary_key=True)
    An_Application_UUID=models.UUIDField(verbose_name='唯一标识符',auto_created=True, default=uuid.uuid1, editable=False)
    An_Application_name=models.CharField(max_length=255,null=False,verbose_name="应用系统名称")
    An_Application_creatDate = models.DateField(default=timezone.now, verbose_name="应用创建日期")

    class Meta:
        verbose_name = "应用系统信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.An_Application_name

class AppMap(models.Model):
    id = models.AutoField(primary_key=True)
    AppMap_name=models.CharField(verbose_name="MAP名称", max_length=128)
    FK_AppMap_Application=models.ForeignKey(to='Application',related_name="AnMap", to_field='id',null=True, blank=True, verbose_name='应用名称',on_delete=models.CASCADE)

    class Meta:
        verbose_name = "应用地图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.AppMap_name


class App3D(models.Model):
    id = models.AutoField(primary_key=True)
    #{'x':123,'y':123,'z':123}
    # xyz=models.CharField(max_length=64,verbose_name="坐标系")
    Asset_UUID = models.UUIDField(verbose_name='资产标识UUID', editable=True)
    x=models.IntegerField(max_length=16,verbose_name="X")
    y=models.IntegerField(max_length=16,verbose_name="Y")
    z=models.IntegerField(max_length=16,verbose_name="Z")
    img=models.ImageField(upload_to='category/%Y/%m', verbose_name='分类图片', null=True, blank=True)
    FK_App3D_AppMap=models.ForeignKey(to='AppMap',related_name="map3d", to_field='id',null=True, blank=True, verbose_name='应用地图关联信息',on_delete=models.CASCADE)

    class Meta:
        verbose_name = "应用3D模型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Asset_UUID

