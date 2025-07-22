def test_register_user(client):
    response = client.post(
        "/register",
        data={
            "username": "test",
            "email": "test@example.com",
            "password": "secret",
            "confirm_password": "secret"
        }
    )
    assert response.status_code == 302
