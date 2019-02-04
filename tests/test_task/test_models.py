import pytest
from server.tasks.models import Task, Project, Description, Comment
from tests.factories import (
    TaskFactory, UserFactory,
    ProjectFactory, DescriptionFactory, CommentFactory
)


@pytest.mark.django_db
def test_create():
    task = TaskFactory.create()
    assert Task.objects.count() == 1
    assert str(task) == task.name


@pytest.mark.django_db
def test_change_executor_and_status():
    executor_1 = UserFactory.create()
    executor_2 = UserFactory.create()
    task = TaskFactory(executor=executor_1)
    assert task.executor == executor_1
    task.executor = executor_2
    task.save()
    assert task.executor == executor_2


@pytest.mark.django_db
def test_delete():
    task = TaskFactory.create()
    assert Task.objects.count() == 1
    task.delete()
    assert Task.objects.count() == 0


@pytest.mark.django_db
def test_add_comment():
    task = TaskFactory.create()
    text_comment = 'test'
    comment = task.add_comment(text_comment)
    assert comment.text == text_comment
    assert task.comments.count() == 1


@pytest.mark.django_db
def test_create_project():
    project = ProjectFactory.create()
    assert Project.objects.count() == 1
    assert str(project) == project.name


@pytest.mark.django_db
def test_create_description():
    description = DescriptionFactory.create()
    assert Description.objects.count() == 1
    assert str(description) == description.text


@pytest.mark.django_db
def test_create_comment():
    comment = CommentFactory.create()
    assert Comment.objects.count() == 1
    assert str(comment) == comment.text
