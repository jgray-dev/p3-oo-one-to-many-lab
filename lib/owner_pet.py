class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def get_type(self):
        return self._pet_type

    def set_type(self, value):
        if value in Pet.PET_TYPES:
            self._pet_type = value
        else:
            raise Exception("Invalid pet type")

    pet_type = property(get_type, set_type)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        if type(pet) is Pet:
            pet.owner = self
        else:
            raise Exception("Pet must be of type Pet")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
