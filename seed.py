from app import create_app, db

from app.models.planet import Planet


my_app = create_app()
with my_app.app_context():
    db.create_all()

    planets = [
        Planet(name="Mercury", description="The smallest planet in our solar system.", color="Gray"),
        Planet(name="Venus", description="The hottest planet in our solar system.", color="Yellow"),
        Planet(name="Earth", description="Our home planet.", color="Blue"),
        Planet(name="Mars", description="The red planet.", color="Red"),
        Planet(name="Jupiter", description="The largest planet in our solar system.", color="Orange"),
        Planet(name="Saturn", description="Known for its beautiful rings.", color="Pale Gold"),
        Planet(name="Uranus", description="An ice giant with a unique tilt.", color="Cyan"),
        Planet(name="Neptune", description="The farthest planet from the Sun.", color="Deep Blue"),
    ]

    db.session.bulk_save_objects(planets)
    db.session.commit()