BASE_URL = "https://jsonplaceholder.typicode.com"

# Keeps track of each route's fields and total count, filterable key (if any), and testing payloads for PUT and POST test cases
RESOURCES = {
    "posts": {
        "count": 100,
        "fields": {"userId": int, "id": int, "title": str, "body": str},
        "filter_key": "userId",
        "new_id": 101,
        "payload": {"userId": 1, "title": "test", "body": "this is a test post"},
        "expected-count": 5,
    },
    "comments": {
        "count": 500,
        "fields": {"postId": int, "id": int, "name": str, "email": str, "body": str},
        "filter_key": "postId",
        "new_id": 501,
        "payload": {"postId": 1, "name": "test name", "email": "test@mail.com", "body": "test body"},
        "expected-count": 500,
    },
    "albums": {
        "count": 100,
        "fields": {"userId": int, "id": int, "title": str},
        "filter_key": "userId",
        "new_id": 101,
        "payload": {"userId": 1, "title": "test album"},
        "expected-count": 500,
    },
    "photos": {
        "count": 5000,
        "fields": {"albumId": int, "id": int, "title": str, "url": str, "thumbnailUrl": str},
        "filter_key": "albumId",
        "new_id": 5001,
        "payload": {
            "albumId": 1,
            "title": "test photo",
            "url": "https://website.com/photo.png",
            "thumbnailUrl": "https://website.com/thumbnail.png",
        },
        "expected-count": 500,
    },
    "todos": {
        "count": 200,
        "fields": {"userId": int, "id": int, "title": str, "completed": bool},
        "filter_key": "userId",
        "new_id": 201,
        "payload": {"userId": 1, "title": "test todo", "completed": False},
        "expected-count": 500,
    },
    "users": {
        "count": 10,
        "fields": {
            "id": int,
            "name": str,
            "username": str,
            "email": str,
            "address": dict,
            "phone": str,
            "website": str,
            "company": dict,
        },
        "filter_key": None,
        "new_id": 11,
        "payload": {"name": "Test User", "username": "testuser", "email": "test@mail.com"},
        "expected-count": 500,
    }
}

COMMENTS = {
    "fields": {"postId": int, "id": int, "name": str, "email": str, "body": str},
    "filter_key": "userId",
}

ALL = list(RESOURCES)