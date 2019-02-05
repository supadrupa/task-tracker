from django.contrib import admin

from server.tasks.models import Comment, Description, Project, Task


class CommentInline(admin.StackedInline):
    '''Stacked Inline View for Comment'''
    model = Comment
    extra = 1


class DescriptionInline(admin.StackedInline):
    '''Stacked Inline View for Description'''
    model = Description
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    '''Admin View for Task'''

    inlines = [
        DescriptionInline,
        CommentInline,
    ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    '''Admin View for Project'''
