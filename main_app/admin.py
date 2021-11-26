from django.contrib import admin
from main_app.models import Appartment, AppartmentImage, Application
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget


class AppartmentImageInline(admin.TabularInline):
    model = AppartmentImage
    readonly_fields = ('image_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

class AppartmentAdmin(admin.ModelAdmin):
    inlines = [AppartmentImageInline]
    list_display = ('address',)


class ApplicationAdmin(admin.ModelAdmin):
     list_display = ('id', 'address', 'phone', 'date_start', 'date_end')

admin.site.register(Appartment, AppartmentAdmin)
admin.site.register(Application, ApplicationAdmin)