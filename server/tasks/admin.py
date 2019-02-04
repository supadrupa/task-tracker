from django.contrib import admin
from server.tasks.models import Task, Description


class DescriptionInline(admin.StackedInline):
    '''Stacked Inline View for Description'''
    model = Description
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    '''Admin View for Task'''

    inlines = [
        DescriptionInline,
    ]
