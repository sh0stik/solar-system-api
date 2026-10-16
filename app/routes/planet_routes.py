from flask import Blueprint, abort, make_response, request, Response

from app.models.planet import Planet

from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


# CREATE
@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    color = request_body["color"]

    new_planet = Planet(name=name, description=description, color=color)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "color": new_planet.color,
    }
    return response, 201


# READ
@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet)

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    color_param = request.args.get("color")
    if color_param:
        query = query.where(Planet.color.ilike(f"%{color_param}%"))

    query = query.order_by(Planet.id)
    planets = db.session.execute(query).scalars()

    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color,
            }
        )
    return planets_response


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "color": planet.color,
    }


# UPDATE
@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"] 
    db.session.commit()

    return Response(status=204, mimetype="application/json")


# DELETE
@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


# HELPER FUNCTION FOR ERROR HANDLING


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.execute(query).scalar()

    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))
    return planet
