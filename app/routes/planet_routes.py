from flask import Blueprint, abort, make_response, request, Response

from app.models.planet import Planet
from app.routes.route_utilities import validate_model

from ..db import db

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


# CREATE
@bp.post("")
def create_planet():
    request_body = request.get_json()

    new_planet = Planet.from_dict(request_body)
    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201


# READ
@bp.get("")
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
        planets_response.append(planet.to_dict())
    return planets_response


@bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()

# UPDATE
@bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"] 
    db.session.commit()

    return Response(status=204, mimetype="application/json")


# DELETE
@bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")
