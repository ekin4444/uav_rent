from django.apps import apps
from django.contrib import admin

from core.models import RentalRecord, DateRange, Lease


# Register your models here.
@admin.register(apps.get_model('core', 'UAV'))
class UAVAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'air_residence_time', 'category')
    list_filter = ('category',)
    search_fields = ('brand', 'model')


@admin.register(DateRange)
class DateRangeAdmin(admin.ModelAdmin):
    pass


@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    search_fields = ('renter',)


@admin.register(apps.get_model('core', 'RentalRecord'))
class RentalRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'uav', 'status', 'return_date')
    list_filter = ('status',)
    search_fields = ('user__username', 'uav__brand', 'uav__model')

    def delete_view(self, request, object_id, extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context['object_name'] = str(RentalRecord._meta.verbose_name)
        return super().delete_view(request, object_id, extra_context=extra_context)
