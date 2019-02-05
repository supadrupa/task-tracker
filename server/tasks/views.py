from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from server.tasks.models import Task, Project, Comment
from server.tasks.serializers import (
    TaskSerializer, ProjectSerializer, CommentSerializer,
    TaskChangeExecutorSerializer, TaskChangeStatusSerializer
)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name',)
    ordering_fields = ('name',)
    filterset_fields = ('id', 'name',)


class TaskViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name', 'project__name')
    filterset_fields = ('name', 'project', 'status', 'executor', 'author')
    serializers = {
        'default': TaskSerializer,
        'change_status': TaskChangeStatusSerializer,
        'change_executor': TaskChangeExecutorSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    @action(detail=True, methods=['patch'])
    def change_status(self, request, pk=None):
        """Change status."""
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['patch'])
    def change_executor(self, request, pk=None):
        """Change executor."""
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('text',)
    ordering_fields = ('text',)
    filterset_fields = ('task',)
