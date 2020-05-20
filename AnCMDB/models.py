from django.db import models

# Create your models here.

class items(models.Model):
    pass

class sys_ports(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(verbose_name="名称", null=False, max_length=64)
    ports = models.CharField(verbose_name="端口", null=False, max_length=128)
    desc=models.TextField(verbose_name="备注",null=True,default="",blank="")

    class Meta:
        verbose_name = "端口列表"
        verbose_name_plural = verbose_name

    # 列表返回的显示
    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name

class sys_IPAddress(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(verbose_name="名称", null=False, max_length=64)
    ipaddress = models.CharField(verbose_name="IP地址", null=False, max_length=128)
    desc=models.TextField(verbose_name="备注",null=True,default="",blank="")

    class Meta:
        verbose_name = "IP地址列表"
        verbose_name_plural = verbose_name

    # 列表返回的显示
    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name

class sys_os(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(verbose_name="名称", null=True, max_length=64)
    os = models.CharField(verbose_name="系统", null=True, max_length=128)
    ver=models.CharField(verbose_name="版本",null=True, max_length=128)
    desc=models.TextField(verbose_name="备注",null=True,default="",blank="")

    class Meta:
        verbose_name = "操作系统"
        verbose_name_plural = verbose_name

    # 列表返回的显示
    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name

class sys_db(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(verbose_name="名称", null=True, max_length=64)
    dbsystem = models.CharField(verbose_name="数据系统", null=True, max_length=128)
    ver=models.CharField(verbose_name="版本",null=True, max_length=128)
    desc=models.TextField(verbose_name="备注",null=True,default="",blank="")

    class Meta:
        verbose_name = "数据库系统"
        verbose_name_plural = verbose_name

    # 列表返回的显示
    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name

class sys_Middleware(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="名称", null=True, max_length=64)
    midd = models.CharField(verbose_name="中间件", null=True, max_length=128)
    ver = models.CharField(verbose_name="版本", null=True, max_length=128)
    desc = models.TextField(verbose_name="备注", null=True, default="", blank="")

    class Meta:
        verbose_name = "中间件"
        verbose_name_plural = verbose_name

    # 列表返回的显示
    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name

class sys_app(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(verbose_name="名称", null=True, max_length=64)
    app = models.CharField(verbose_name="应用系统", null=True, max_length=128)
    ver=models.CharField(verbose_name="版本",null=True, max_length=128)
    desc=models.TextField(verbose_name="备注",null=True,default="",blank="")

    class Meta:
        verbose_name = "应用系统"
        verbose_name_plural = verbose_name

    # 列表返回的显示
    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name

