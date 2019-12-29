from django.contrib import admin
from .models import Moment, Comment


class MomentAdmin(admin.ModelAdmin):
    empty_value_display = '空值'


class MyAdminSite(admin.AdminSite):
    site_header = '我的管理网站'
    site_url = '/app/moments_input'


admin_site = MyAdminSite()
# admin.site.register(Moment)
admin_site.register(Comment)
admin_site.register(Moment, MomentAdmin)