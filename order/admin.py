

from django.contrib import admin
from .models import Item, ItemImage , Item2, ItemImage2, Item3, ItemImage3

class ItemImageAdmin(admin.ModelAdmin):
    list_display = ('item', 'image')  # الحقول التي ستظهر في قائمة الصور الإضافية

admin.site.register(ItemImage, ItemImageAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name_item', 'description', 'area_in_meters', 'added_by')
    search_fields = ('name_item', 'description')

admin.site.register(Item, ItemAdmin)



class ItemImageAdmin(admin.ModelAdmin):
    list_display = ('item', 'image')  # الحقول التي ستظهر في قائمة الصور الإضافية

admin.site.register(ItemImage2, ItemImageAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name_item', 'description', 'area_in_meters', 'added_by')
    search_fields = ('name_item', 'description')

admin.site.register(Item2, ItemAdmin)



class ItemImageAdmin(admin.ModelAdmin):
    list_display = ('item', 'image')  # الحقول التي ستظهر في قائمة الصور الإضافية

admin.site.register(ItemImage3, ItemImageAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name_item', 'description', 'area_in_meters', 'added_by')
    search_fields = ('name_item', 'description')

admin.site.register(Item3, ItemAdmin)



