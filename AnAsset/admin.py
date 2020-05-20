from django.contrib import admin
from .models import *

# Register your models here.
class MovieApiSourceAdmin(admin.ModelAdmin):
    # 需要显示的字段信息
    list_display = ('id', 'api_name', 'api_url', 'sdata','lv','version','status')

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('id', 'api_name', 'api_url', 'sdata','lv','version','status')

    # 后台搜索字段
    search_fields=('api_name','api_url')

    #后台排序字段
    list_filter=('id','api_name','api_url','lv','version','status')

    #默认排序
    ordering=('id','api_url')

admin.site.register(Asset)
admin.site.register(Asset_type)
admin.site.register(Asset_Racks)
admin.site.register(Asset_engine_room)
admin.site.register(Asset_IT_hosts)
admin.site.register(software)
admin.site.register(software_type)
admin.site.register(network_device)
admin.site.register(Network_security_equipment)
