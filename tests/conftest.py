import pytest

from .resources import BASE_URL

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

# Checks that every expected key exists with the expected type.
def assert_fields(obj: dict, fields: dict):
    for key, expected_type in fields.items():
        assert key in obj, f"missing field '{key}' in {obj}"
        value = obj[key]
        if expected_type is int:
            # Checks that values that are supposed to be int are not actually bools (False returns 0, True returns 1)
            assert isinstance(value, int) and not isinstance(value, bool), \
                f"'{key}' = {value!r}, expected int"
        else:
            assert isinstance(value, expected_type), \
                f"'{key}' = {value!r}, expected {expected_type.__name__}"