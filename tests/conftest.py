import pytest
import factory
from pytest_factoryboy import register
from rest_framework.test import APIClient

from tests.factories import (CommentFactory, DescriptionFactory,
                             ProjectFactory, TaskFactory, UserFactory)


register(TaskFactory)
register(UserFactory)
register(ProjectFactory)
register(CommentFactory)
register(DescriptionFactory)


@pytest.fixture
def apiclient():
    return APIClient()


@pytest.fixture
def task_factory_by_dict():
    return factory.build(dict, FACTORY_CLASS=TaskFactory)
