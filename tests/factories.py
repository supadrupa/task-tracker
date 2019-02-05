from django.contrib.auth import get_user_model

import factory

from server.tasks.models import Comment, Description, Project, Task


User = get_user_model()


class UserFactory(factory.DjangoModelFactory):
    """
    Define User Factory
    """
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(
        lambda a: '{0}.{1}@example.com'.format(
            a.first_name, a.last_name).lower())
    username = factory.Sequence(lambda n: 'username_%s' % n)


class ProjectFactory(factory.DjangoModelFactory):
    """
    Define Project Factory
    """
    class Meta:
        model = Project


class TaskFactory(factory.DjangoModelFactory):
    """
    Define Task Factory
    """
    class Meta:
        model = Task

    executor = factory.SubFactory(UserFactory)
    author = factory.SubFactory(UserFactory)
    project = factory.SubFactory(ProjectFactory)


class DescriptionFactory(factory.DjangoModelFactory):
    """
    Define Description Factory
    """
    class Meta:
        model = Description

    task = factory.SubFactory(TaskFactory)


class CommentFactory(factory.DjangoModelFactory):
    """
    Define Comment Factory
    """
    class Meta:
        model = Comment

    task = factory.SubFactory(TaskFactory)
