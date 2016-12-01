class Animal(object):
    GROWTH_SCALE = (
        ("Old", 51),
        ("Mature", 36),
        ("Young", 21),
        ("Child", 11),
        ("Baby", 2),
        ("Born", 1)
    )

    def __init__(self, name, growth_rate, food_need, water_need):
        self.name = name
        self._weight = 1
        self._days_growing = 0
        self._type = "generic"
        self._status = "Born"
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need

    def needs(self): return {"Food need": self._food_need, "Water need": self._water_need}

    def report(self):
        return {
            "Name": self.name,
            "Type": self._type,
            "Status": self._status,
            "Days growing": self._days_growing,
            "Weight: ": self._weight
        }

    def _update_status(self):
        for item in self.GROWTH_SCALE:
            if self._weight >= item[1]:
                self._status = item[0]
                break

    def grow(self, available_food, available_water):
        if available_food >= self._food_need and available_water >= self._water_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()

class Cow(Animal):
    def __init__(self, name):
        super(Cow, self).__init__(name, 3, 5, 4)
        self._type = 'Cow'

    def grow(self, available_food, available_water):
        if available_food >= self._food_need and available_water >= self._water_need:
            if self._status == 'Born':
                self._weight += self._growth_rate * 1.5
            elif self._status == 'Baby':
                self._weight += self._growth_rate * 1.5
            elif self._status == 'Child':
                self._weight += self._growth_rate * 1.25
            elif self._status == 'Young':
                self._weight += self._growth_rate
            elif self._status == 'Mature':
                self._weight += self._growth_rate
            elif self._status == 'Old':
                self._weight += self._growth_rate * 0.75
        self._days_growing += 1
        self._update_status()


class Sheep(Animal):
    def __init__(self, name):
        super(Sheep, self).__init__(name, 5, 3, 3)
        self._type = 'Cow'

    def grow(self, available_food, available_water):
        if available_food >= self._food_need and available_water >= self._water_need:
            if self._status == 'Born':
                self._weight += self._growth_rate * 1.4
            elif self._status == 'Baby':
                self._weight += self._growth_rate * 1.3
            elif self._status == 'Child':
                self._weight += self._growth_rate
            elif self._status == 'Young':
                self._weight += self._growth_rate
            elif self._status == 'Mature':
                self._weight += self._growth_rate
            elif self._status == 'Old':
                self._weight += self._growth_rate * 0.5
        self._days_growing += 1
        self._update_status()

if __name__ == "__main__":
    animal = Animal('Petya', 3, 4, 4)
    print animal.report()
    print animal.name
    animal.name = 'Vanya'
    print animal.needs()
    animal._weight = 5
    animal._update_status()
    print animal.report()
    animal._weight = 25
    animal._update_status()
    print animal.report()
    animal.grow(4, 4)
    print animal.report()