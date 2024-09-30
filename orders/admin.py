from django.contrib import admin
from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'book', 'status', 'city', 'created_at']
    list_filter = ['status']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['name'].disabled = True
            form.base_fields['address'].disabled = True
            form.base_fields['city'].disabled = True
            form.base_fields['phone_number'].disabled = True
        return form
