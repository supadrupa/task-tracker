from rest_framework import serializers

from server.tasks.models import Description, Project, Task, Comment


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ('id', 'text',)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'task', 'text',)


class TaskSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    descriptions = DescriptionSerializer(many=True)

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'project', 'status',
            'executor', 'author', 'descriptions', 'comments'
        )

    def create(self, validated_data):
        descriptions = validated_data.pop('descriptions')
        task = Task.objects.create(**validated_data)
        for description in descriptions:
            Description.objects.create(task=task, **description)
        return task


class TaskChangeExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('executor',)


class TaskChangeStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('status',)
