from django.contrib import admin
from .models import SocietyRecord
@admin.register(SocietyRecord)
class SocietyRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "title", "created_at")
    list_filter = ("category",)
    search_fields = ("title", "category")
