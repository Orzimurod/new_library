from django.contrib import admin
from shop.models import Author, Book, Genre


class AddDeleteVievMixin:

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request, obj=None) -> bool:
        return True

    def has_delete_permission(self, request, obj=None) -> bool:
        return True

    def has_view_permission(self, request, obj=None) -> bool:
        return True


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = "date_published"
    list_display = ['title', 'date_published', 'price', 'description']
    fields = ['title', 'price', 'description']


admin.site.register(Genre)
# admin.site.register(Author)


@admin.register(Author)
class Author(AddDeleteVievMixin, admin.ModelAdmin):
    pass
