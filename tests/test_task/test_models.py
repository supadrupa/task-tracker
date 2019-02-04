import pytest
from server.tasks.models import Task
from tests.factories import TaskFactory, UserFactory


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
    pass
