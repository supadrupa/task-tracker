import pytest
from server.tasks.models import Task


@pytest.mark.django_db
def test_get(apiclient):
    response = apiclient.get('/api/tasks/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_detail(apiclient, task_factory):
    data = task_factory.create()
    response = apiclient.get('/api/tasks/{}/'.format(data.pk))
    assert response.status_code == 200


@pytest.mark.django_db
def test_change_executor(apiclient, task_factory, user_factory):
    old_executor = user_factory.create()
    new_executor = user_factory.create()
    data = task_factory.create(executor=old_executor)
    response = apiclient.patch(
        '/api/tasks/{}/change_executor/'.format(data.pk),
        data={"executor": new_executor.pk}
    )
    task = Task.objects.get(pk=data.pk)
    assert task.executor.pk == new_executor.pk
    assert response.status_code == 200


@pytest.mark.django_db
def test_change_status(apiclient, task_factory):
    data = task_factory.create()
    response = apiclient.patch(
        '/api/tasks/{}/change_status/'.format(data.pk),
        data={"status": 2}
    )
    task = Task.objects.get(pk=data.pk)
    assert task.status == 2
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete(apiclient, task_factory):
    data = task_factory.create()
    response = apiclient.delete('/api/tasks/{}/'.format(data.pk))
    assert response.status_code == 204
