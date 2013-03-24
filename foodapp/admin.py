from django.contrib import admin

from models import Item, Order

class ItemAdmin(admin.ModelAdmin):
    actions = ['mark_once_a_day', 'mark_not_once_a_day']

    def mark_once_a_day(self, request, queryset):
        rows_updated = queryset.update(once_a_day=True)
        if rows_updated == 1:
            message_bit = "1 item was"
        else:
            message_bit = "%s items were" % rows_updated
        self.message_user(request, "%s successfully set as once a day." % message_bit)
    mark_once_a_day.short_description = "Mark selected items as 'once_a_day'."
    
    def mark_not_once_a_day(self, request, queryset):
        rows_updated = queryset.update(once_a_day=False)
        if rows_updated == 1:
            message_bit = "1 item was"
        else:
            message_bit = "%s items were" % rows_updated
        self.message_user(request, "%s successfully set as not once a day." % message_bit)
    mark_not_once_a_day.short_description = "Mark selected items as not 'once_a_day'."

class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_filter = ('user', 'date', 'item')
    list_display = ('user', 'date', 'item', 'quantity')

admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)

