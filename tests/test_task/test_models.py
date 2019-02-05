import pytest
from server.tasks.models import Task, Project, Description, Comment


@pytest.mark.django_db
def test_create(task_factory):
    task = task_factory.create()
    assert Task.objects.count() == 1
    assert str(task) == task.name


@pytest.mark.django_db
def test_change_executor_and_status(task_factory, user_factory):
    executor_1 = user_factory.create()
    executor_2 = user_factory.create()
    task = task_factory(executor=executor_1)
    assert task.executor == executor_1
    task.executor = executor_2
    task.save()
    assert task.executor == executor_2


@pytest.mark.django_db
def test_delete(task_factory):
    task = task_factory.create()
    assert Task.objects.count() == 1
    task.delete()
    assert Task.objects.count() == 0


@pytest.mark.django_db
def test_add_comment(task_factory):
    task = task_factory.create()
    text_comment = 'test'
    comment = task.add_comment(text_comment)
    assert comment.text == text_comment
    assert task.comments.count() == 1


@pytest.mark.django_db
def test_create_project(project_factory):
    project = project_factory.create()
    assert Project.objects.count() == 1
    assert str(project) == project.name


@pytest.mark.django_db
def test_create_description(description_factory):
    description = description_factory.create()
    assert Description.objects.count() == 1
    assert str(description) == description.text


@pytest.mark.django_db
def test_create_comment(comment_factory):
    comment = comment_factory.create()
    assert Comment.objects.count() == 1
    assert str(comment) == comment.text
