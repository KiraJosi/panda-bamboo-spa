class Customer:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species  # z.B. "Fox", "Deer", "Raccoon"

    def to_dict(self):
        return {
            "name": self.name,
            "species": self.species
        }

    @staticmethod
    def from_dict(data: dict):
        return Customer(
            name=data["name"],
            species=data["species"]
        )

