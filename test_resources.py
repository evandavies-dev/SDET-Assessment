import pytest, requests

from .conftest import assert_fields
from .resources import ALL, RESOURCES, COMMENTS

FILTERABLE = [n for n in ALL if RESOURCES[n]["filter_key"]]

# Testing GET on all routes
@pytest.mark.parametrize("name", ALL)
def test_get_route(base_url, name):
    r = requests.get(f"{base_url}/{name}", timeout=10)
    assert r.status_code == 200
    items = r.json()
    assert len(items) == RESOURCES[name]["count"]
    assert_fields(items[0], RESOURCES[name]["fields"])

# Testing GET on all routes' /1
@pytest.mark.parametrize("name", ALL)
def test_get_one(base_url, name):
    r = requests.get(f"{base_url}/{name}/1", timeout=10)
    assert r.status_code == 200
    assert r.json()["id"] == 1
    assert_fields(r.json(), RESOURCES[name]["fields"])

# Testing GET on all routes' comments
@pytest.mark.parametrize("name", ALL)
def test_get_one_comment(base_url, name):
    r = requests.get(f"{base_url}/{name}/1/comments", timeout=10)
    assert r.status_code == 200
    comments = r.json()
    assert len(comments) == RESOURCES[name]["expected-count"] # Every route's /1/comments page returns 500 comments, except for posts/1/comments which returns 5. This expected comment count is included for each route in resources.py
    for comment in comments:
        assert_fields(comment, COMMENTS["fields"])

# Testing POST on all routes
@pytest.mark.parametrize("name", ALL)
def test_post(base_url, name):
    payload = RESOURCES[name]["payload"]
    r = requests.post(f"{base_url}/{name}", json=payload, timeout=10)
    assert r.status_code == 201
    assert r.json()["id"] == RESOURCES[name]["new_id"]

# Testing PUT on all routes
@pytest.mark.parametrize("name", ALL)
def test_put(base_url, name):
    r = requests.put(f"{base_url}/{name}/1", json=RESOURCES[name]["payload"], timeout=10)
    assert r.status_code == 200
    assert r.json()["id"] == 1

# Testing PATCH on all routes
@pytest.mark.parametrize("name", ALL)
def test_patch(base_url, name):
    r = requests.patch(f"{base_url}/{name}/1", json={"title": "patched"}, timeout=10)
    assert r.status_code == 200
    assert r.json()["title"] == "patched"

# Testing DELETE on all routes
@pytest.mark.parametrize("name", ALL)
def test_delete(base_url, name):
    r = requests.delete(f"{base_url}/{name}/1", timeout=10)
    assert r.status_code == 200

# Testing invalid Routes
@pytest.mark.parametrize("name", ALL)
@pytest.mark.parametrize("bad_id", ["0", "QWERTY", "9999999"])
def test_get_invalid_id_returns_404(base_url, name, bad_id):
    r = requests.get(f"{base_url}/{name}/{bad_id}", timeout=10)
    assert r.status_code == 404

# Testing filterable routes (example: /comments?postId=1)
@pytest.mark.parametrize("name", FILTERABLE)
def test_filter_by_parent_id(base_url, name):
    key = RESOURCES[name]["filter_key"]
    items = requests.get(f"{base_url}/{name}", params={key: 1}, timeout=10).json()
    assert items
    assert all(i[key] == 1 for i in items)

# Testing nested route paths
@pytest.mark.parametrize("path, expected", [
    ("/albums/1/posts", 100),
    ("/photos/1/users", 10),
    ("/todos/1/todos", 200),
    ("/comments/1/photos", 5000),
    ("/users/1/albums", 10),
])
def test_nested_routes(base_url, path, expected):
    r = requests.get(f"{base_url}{path}", timeout=10)
    assert r.status_code == 200
    assert len(r.json()) == expected