from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _


class Project(models.Model):
    """Model definition for Project."""

    name = models.CharField(_('name'), max_length=50)

    class Meta:
        """Meta definition for Project."""

        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        """Unicode representation of Project."""
        return self.name


class Task(models.Model):
    OPEN = 1
    CLOSED = 2
    STATUS = (
        (OPEN, _('Open')),
        (CLOSED, _('Сlosed')),
    )

    name = models.CharField(_('name'), max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.PositiveIntegerField(
        _('status'),
        choices=STATUS,
        default=OPEN)
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='executor_tasks',
        verbose_name=_('executor')
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author_tasks',
        verbose_name=_('author')
    )

    class Meta:
        """Meta definition for Task."""

        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        """Unicode representation of Task."""
        return self.name


class Description(models.Model):
    """Model definition for Description."""
    text = models.CharField(_('text'), max_length=255)
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='descriptions',
        verbose_name=_('task')
    )

    class Meta:
        """Meta definition for Description."""

        verbose_name = _('Description')
        verbose_name_plural = _('Descriptions')

    def __str__(self):
        """Unicode representation of Description."""
        return self.text
