def test_get(apiclient):
    response = apiclient.get('/api/tasks/')
    assert response.status_code == 200


def test_create(apiclient):
    response = apiclient.post('/api/tasks/')
    assert response.status_code == 201


def test_detail(apiclient):
    response = apiclient.get('/api/tasks/1/')
    assert response.status_code == 200


def test_update(apiclient):
    response = apiclient.put('/api/tasks/1/')
    assert response.status_code == 200


def test_delete(apiclient):
    response = apiclient.delete('/api/tasks/1/')
    assert response.status_code == 204


def test_adds_comment(apiclient):
    response = apiclient.post('/api/tasks/1/add_comment/')
    assert response.status_code == 201
