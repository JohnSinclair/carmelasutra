from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateTimeWidget
from import_export.admin import ImportExportMixin
from django.utils.safestring import mark_safe
from .models import *
import admin_thumbnails



class PictureResource(resources.ModelResource):
    class Meta:
        model = Picture

class PictureCollectionResource(resources.ModelResource):
    class Meta:
        model = PictureCollection

class CVResource(resources.ModelResource):
    class Meta:
        model = CourseOfLife



# @admin_thumbnails.thumbnail('upload')
class PictureAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = PictureResource


# @admin_thumbnails.thumbnail('thumbnail')
class PictureCollectionAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = PictureCollectionResource
    # fields = ( 'thumbnails',  )
    readonly_fields = ('thumbnails',)

class CVAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = CVResource


admin.site.register(Picture, PictureAdmin)
admin.site.register(PictureCollection, PictureCollectionAdmin)
admin.site.register(CourseOfLife, CVAdmin)
