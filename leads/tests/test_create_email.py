import requests


def test_cerate_email_status_code():
    payload = {"name": "lid", "email": "user@teste2.com"}
    r = requests.post("http://127.0.0.1:8000/api/v1/email/", data=payload)
    assert r.status_code == 201


def test_exist_email_status_code():
    payload = {"name": "lid", "email": "user@teste.com"}
    r = requests.post("http://127.0.0.1:8000/api/v1/email/", data=payload)
    assert r.status_code == 409


def test_find_email():
    payload = {"email": "user@teste.com"}
    r = requests.get("http://127.0.0.1:8000/api/v1/email/", data=payload)
    assert r.status_code == 200
