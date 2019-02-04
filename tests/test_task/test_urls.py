def test_get(client):
    response = client.get('/api/tasks/')
    assert response.status_code == 200


def test_create(client):
    response = client.post('/api/tasks/')
    assert response.status_code == 201


def test_detail(client):
    response = client.get('/api/tasks/1/')
    assert response.status_code == 200


def test_update(client):
    response = client.put('/api/tasks/1/')
    assert response.status_code == 200


def test_delete(client):
    response = client.delete('/api/tasks/1/')
    assert response.status_code == 204


def test_adds_comment(client):
    response = client.post('/api/tasks/1/add_comment/')
    assert response.status_code == 201
