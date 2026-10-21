from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db import db


class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    size: Mapped[int]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")

    def to_dict(self):
        moon_as_dict = {}
        moon_as_dict["id"] = self.id
        moon_as_dict["name"] = self.name
        moon_as_dict["description"] = self.description
        moon_as_dict["size"] = self.size

        if self.planet:
            moon_as_dict["planet"] = self.planet.name
            
        return moon_as_dict

    @classmethod
    def from_dict(cls, planet_data):
        planet_id = planet_data.get("planet_id")

        new_moon = cls(name=planet_data["name"],
                         description=planet_data["description"],
                         size=planet_data["size"],
                         planet_id=planet_id)
        return new_moon