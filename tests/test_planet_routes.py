def test_get_one_planet(client):
    #Act 
    response = client.get("/planets/1")
    planet = response.get_json()

    #Assert 
    assert response.status_code == 200
    assert planet == {
        "id": "",
        "name": "",
        "description": "",
        "color": ""
    }
    



# def test_get_all_planets(client):
#    #Act 


#    #Assert
# assert planets["id"] == three_planets.id
#     assert planets["name"] == three_planets.name
#     assert planets["description"] == three_planets.description
#     assert planets["color"] == three_planets.color
