def test_create_user(django_user_model):
    username = "username"
    password = "password"
    django_user_model.objects.create_user(username=username, password=password)
    assert django_user_model.objects.get(username=username).username == username


def test_create_super_user(django_user_model):
    username = "super_username"
    email = 'email@email.com'
    password = "super_password"
    django_user_model.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    assert django_user_model.objects.get(username=username).username == username
