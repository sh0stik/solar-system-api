def test_get_planets_with_no_records(client):
    # Act 
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_return_successfully(client, three_planets):
    # Arrange
    expected_planet = three_planets[0]
    
    # Act
    response = client.get("/planets/1")
    planet = response.get_json()

    # Assert
    assert response.status_code == 200
    assert planet["id"] == expected_planet.id
    assert planet["name"] == expected_planet.name
    assert planet["description"] == expected_planet.description
    assert planet["color"] == expected_planet.color

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
        {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color,
        }
        for planet in three_planets
    ]

def test_create_planet_successfully(client):
    # Arrange
    expected_planet = {
        "name": "Earth",
        "description": "Our home planet.",
        "color": "Blue"
    }

    # Act
    response = client.post("/planets", json=expected_planet)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body["id"] == 1
    assert response_body["name"] == expected_planet["name"]
    assert response_body["description"] == expected_planet["description"]
    assert response_body["color"] == expected_planet["color"]


def test_moon_to_dict_includes_planet_name(one_moon):
    result = one_moon.to_dict()
 
    assert result == {
        "id": one_moon.id,
        "name": "Phobos",
        "description": "Mars's largest moon.",
        "size": 22,
        "planet": "Mars",
    }