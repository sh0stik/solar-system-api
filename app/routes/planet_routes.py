from flask import Blueprint, abort, make_response, request, Response

from app.models.planet import Planet
from app.models.moon import Moon
from app.routes.route_utilities import validate_model, create_model_with_response, get_models_with_filters_with_response

from ..db import db

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


# CREATE
@bp.post("")
def create_planet():
    request_body = request.get_json()
    return create_model_with_response(Planet, request_body)


# READ
@bp.get("")
def get_all_planets():
    return get_models_with_filters_with_response(Planet, request.args)


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


# NESTED ROUTES

@bp.post("/<planet_id>/moons")
def create_moon_with_planet_id(planet_id):
    planet = validate_model(Planet, planet_id)
    
    request_body = request.get_json()
    request_body["planet_id"] = planet.id
    return create_model_with_response(Moon, request_body)


@bp.get("/<planet_id>/moons")
def get_all_planet_moons(planet_id):
    planet = validate_model(Planet, planet_id)
    moons = [moon.to_dict() for moon in planet.moons]

    return moons