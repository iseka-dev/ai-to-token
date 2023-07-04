def test_get_health_check_route(client):
    response = client.get("/health-check")

    assert response.status_code == 200
    assert response.json() == {
        "check": {"server": "OK", "database": "OK"}
    }
