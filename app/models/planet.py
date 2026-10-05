class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

planets = [Planet(1, "Mercury", "Mercury is the smallest planet in theSolar System"),
           Planet(2, "Earth", "Earth is the third planet from the Sun and the only known world in the universe to harbor life, featuring vast liquid oceans, a breathable atmosphere, and a dynamic surface."),
           Planet(3, "Jupiter", "The largest planet in our solar system, Jupiter is a massive gas giant composed mostly of hydrogen and helium"),
           Planet(4, "Saturn", "Saturn is a gas giant best known for its extensive and dazzling system of icy rings."),
           ]