def test_get_index_html_success(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.is_success
    assert response.template.name == "index.html"
