from rest_framework import serializers


class TaskDescriptionSerializer(serializers.Serializer):
    description = serializers.CharField()


class TaskSerializer(serializers.Serializer):
    """ Название задачи, Проект, Статус, Исполнитель, Автор, Описание. """

    name = serializers.CharField()
    project = serializers.CharField()
    status = serializers.CharField()
    executor = serializers.CharField()
    autor = serializers.CharField()
    description = TaskDescriptionSerializer(many=True)
