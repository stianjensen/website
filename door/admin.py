from django.contrib import admin

from .models import Door, DoorData


@admin.register(Door)
class DoorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Status', {
            'fields': [
                'name',
            ]
        })
    ]
    search_fields = [
        'title'
    ]


@admin.register(DoorData)
class DoorDataAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Data', {
            'fields': [
                'opened',
                'closed',
            ]
        })
    ]
    search_fields = [
        'opened'
    ]
