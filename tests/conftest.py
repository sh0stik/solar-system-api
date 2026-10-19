import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
from app.models.planet import Planet
import os

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def three_planets(app):
    # Arrange
    mars = Planet(name="Mars", description="The red planet.", color="Red")
    mercury = Planet(name="Mercury", description="The smallest planet in our solar system.", color="Gray")
    venus = Planet(name="Venus", description="The hottest planet in our solar system.", color="Yellow")

    db.session.add_all([mars, mercury, venus])
    db.session.commit()
