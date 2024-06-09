import pytest

from data_golf.client import DataGolfClient


@pytest.fixture(scope="function")
def dg_client() -> DataGolfClient:
    yield DataGolfClient(api_key="test_key")
