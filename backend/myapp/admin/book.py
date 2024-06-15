from django.contrib import admin
from myapp import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    icon_name = "icons/imagenes"
    fields = (
        ("title"),
        ("author"),
        ("summary"),
        ("pos_date"),
        ("active"),
    )
    list_display = ["title", "author", "summary", "pos_date", "active"]
    list_display_links = ["title", "author"]
    search_fields = ["title", "author", "summary"]
    list_filter = ["active"]