import pytest
from core.backend import Backend


@pytest.fixture
def json_client():
    return Backend()
