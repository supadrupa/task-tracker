from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


class TaskViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(status=status.HTTP_200_OK)

    def create(self, request):
        return Response(status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        return Response(status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        return Response(status=status.HTTP_201_CREATED)
