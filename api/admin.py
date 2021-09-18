from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Contact, ProductImage

# Setting Admin Panel Custom Header
admin.site.site_header = "Aradhya Outfitters Admin"
admin.site.site_title = "Aradhya Outfitters Admin Site"
admin.site.index_title = "Aradhya Outfitters Admin"

# Removing the default groups
admin.site.unregister(Group)


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Contacts"

    list_display = ('name', 'phone', 'email', 'subject', 'message')

    def has_add_permission(self, request):
        return False


class ProductImagesAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Product Images"

    list_display = ('product_name', 'product_image')


admin.site.register(Contact, ContactAdmin)
admin.site.register(ProductImage, ProductImagesAdmin)
