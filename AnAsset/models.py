from django.db import models
import django.utils.timezone as timezone
import uuid
import json
# from django.contrib.postgres.fields import JSONField
# from django_mysql.models import JSONField


# Create your models here.
class Asset(models.Model):
    """
        资产信息表，所有资产公共信息
    """
    id = models.AutoField(primary_key=True)
    Asset_UUID=models.UUIDField(verbose_name='唯一标识符',auto_created=True, default=uuid.uuid1, editable=False)
    Asset_name=models.CharField(verbose_name="资产名",null=False,max_length=128)
    Asset_creatDate = models.DateField(default = timezone.now,verbose_name="资产启用日期")
    Asset_retirement_date=models.DateField(verbose_name="资产报废日期",null=True,blank=True)
    Asset_isretirement=models.BooleanField(default=False,blank=False,null=True,verbose_name='报废状态|是|否')
    Asset_note=models.TextField(null=True,verbose_name='资产描述',default='',blank=True)
    Asset_type_tid = models.ForeignKey(to='Asset_type', related_name="tid",to_field='id', on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name="资产类型")

    class Meta:
        verbose_name="资产表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Asset_name

class Asset_type(models.Model):
    """
        资产类别信息表，所有资产公共信息
    """
    id = models.AutoField(primary_key=True)
    Asset_type_name = models.CharField(verbose_name="资产类型", max_length=128)
    Asset_type_desc=models.CharField(max_length=500, verbose_name='分类描述',blank=True)
    Asset_sort = models.IntegerField(default=0, verbose_name='排序值')
    Asset_parent = models.ForeignKey('self', default=0, null=True, blank=True, related_name='children', verbose_name='上级分类',on_delete=models.SET_DEFAULT)
    image = models.ImageField(upload_to='category/%Y/%m', verbose_name='分类图片', null=True, blank=True)

    class Meta:
        verbose_name = "资产类型表"
        verbose_name_plural = verbose_name

    # 列表返回的显示
    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.Asset_type_name

class Asset_Extended_tempalte(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=64,verbose_name="扩展信息模板名称")
    '''
    todo : 实现json字段存储，实现自定义
    '''
    # Ejson=JSONField()

    class Meta:
        verbose_name = "资产扩展模板表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Asset_Extended(models.Model):
    id = models.AutoField(primary_key=True)
    Asset_Extended_UUID = models.UUIDField(verbose_name='扩展信息唯一标识符', auto_created=True, default=uuid.uuid1, editable=False)
    eid=models.ForeignKey(to='Asset',to_field='id',on_delete=models.CASCADE)
    # Ejson=JSONField()

    class Meta:
        verbose_name = "资产扩展信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.eid

#机柜
class Asset_Racks(models.Model):
    id = models.AutoField(primary_key=True)
    Racks_name=models.CharField(verbose_name="机柜名称",null=False,max_length=128)
    Racks_model=models.CharField(verbose_name="机柜",null=True,max_length=128)
    Racks_type=models.CharField(verbose_name="机柜型号",null=True,max_length=128)
    Racks_address=models.CharField(verbose_name="机柜位置",null=True,max_length=128)
    Racks_company=models.CharField(verbose_name="机柜厂家",null=True,max_length=128)
    Fk_Asset_Racks=models.ForeignKey(to='Asset', related_name="Fk_Asset_Racks_id",to_field='id', on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name="机柜资产关联")

    class Meta:
        verbose_name = "机柜信息表"
        verbose_name_plural = verbose_name

    # 列表返回的显示
    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.Racks_name

# IT行业特有
class Asset_engine_room(models.Model):
    id = models.AutoField(primary_key=True)
    engine_room_name=models.CharField(verbose_name="机房名称",null=False,max_length=32)
    engine_room_address=models.CharField(verbose_name="机房地址",null=True,max_length=128)
    engine_room_area=models.CharField(verbose_name="机房面积",null=True,max_length=128)
    # longitudes=models.DecimalField(verbose_name="经度",null=True,)
    # latitudes=models.DecimalField(verbose_name="纬度",null=True)

    class Meta:
        verbose_name = verbose_name_plural =u"机房信息表"

    # 列表返回的显示
    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.engine_room_name

class Asset_IT_hosts(models.Model):
    """
        主机信息
    """
    id = models.AutoField(primary_key=True)
    host_name = models.CharField("主机名",max_length=128)
    host_internet = models.IntegerField(verbose_name='网卡数', null=True, blank=True)
    host_ip = models.GenericIPAddressField(verbose_name="IP地址",default="127.0.0.1")
    host_mask = models.GenericIPAddressField(verbose_name="掩码",default="127.0.0.1",null=True, blank=True)
    host_gateway = models.GenericIPAddressField(verbose_name="网关",null=True, blank=True)
    host_dns1 = models.GenericIPAddressField("DNS1",null=True, blank=True)
    host_notes = models.TextField(null=True, blank=True)
    host_createDate = models.DateTimeField(verbose_name="创建日期")
    host_sn = models.CharField(verbose_name='SN号', max_length=64, db_index=True,null=True, blank=True)
    host_manufacturer = models.CharField(verbose_name='制造商', max_length=64, null=True, blank=True)
    host_model = models.CharField(verbose_name='型号', max_length=64, null=True, blank=True)
    host_os_platform = models.CharField(verbose_name='系统', max_length=16, null=True, blank=True)
    host_os_version = models.CharField(verbose_name='系统版本', max_length=16, null=True, blank=True)
    host_manager_ip = models.GenericIPAddressField(verbose_name='管理IP', null=True, blank=True)
    host_cpu_count = models.IntegerField(verbose_name='CPU个数', null=True, blank=True)
    host_cpu_physical_count = models.IntegerField(verbose_name='CPU物理个数', null=True, blank=True)
    host_cpu_model = models.CharField(verbose_name='CPU型号', max_length=128, null=True, blank=True)
    host_memory = models.IntegerField(verbose_name="内存",null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural =u"主机信息表"

    def __str__(self):
        return self.host_name

#软件信息
class software(models.Model):
    id = models.AutoField(primary_key=True)
    software_name=models.CharField(verbose_name="软件名称",max_length=128)
    software_type=models.CharField(verbose_name="软件类型",max_length=128)
    software_company=models.CharField(verbose_name="软件公司",max_length=128)

    class Meta:
        verbose_name = "软件信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.software_name

#软件类别
class software_type(models.Model):
    id = models.AutoField(primary_key=True)
    software_tid=models.ForeignKey(to='software', related_name="tid",to_field='id', on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name="软件资产类型")
    software_type_name=models.CharField("软件类型",max_length=128)

    class Meta:
        verbose_name = "软件类型信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.software_type_name

#网络设备
class network_device(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "网络设备信息表"
        verbose_name_plural = verbose_name

#网络安全设备
class Network_security_equipment(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "安全设备信息表"
        verbose_name_plural = verbose_name

#网络安全设备
class other(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "安全设备信息表"
        verbose_name_plural = verbose_name







