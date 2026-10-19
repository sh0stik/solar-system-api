def test_get_planets_with_no_records(client):
    # Act 
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_return_successfully(client, three_planets):
    # Act
    response = client.get("/planets/1")
    planet = response.get_json()

    # Assert
    assert response.status_code == 200
    assert planet["id"] == 1
    assert planet["name"] == "Mars"
    assert planet["description"] == "The red planet."
    assert planet["color"] == "Red"
    

def test_get_one_planet_return_404(client):
    # Act 
    response = client.get("/planets/1")

    # Assert 
    assert response.status_code == 404

def test_get_all_planets(client, three_planets):
    # Act 
    response = client.get("/planets")
    planets = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(planets) == 3
    assert planets == [
        {"id": 1,
        "name": "Mars",
        "description": "The red planet.",
        "color": "Red"},
        {"id": 2,
        "name": "Mercury",
        "description": "The smallest planet in our solar system.",
        "color": "Gray"},
        {"id": 3,
        "name": "Venus",
        "description": "The hottest planet in our solar system.",
        "color": "Yellow"}
        ]
    