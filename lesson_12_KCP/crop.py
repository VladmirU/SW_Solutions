import random
import os


class Crop(object):
    GROWTH_SCALE = (
        ("Old", 16),
        ("Mature", 11),
        ("Young", 6),
        ("Seeding", 1),
        ("Seed", 0)
    )

    #constructor
    def __init__(self, growth_rate, light_need, water_need):
        self._growth = 0
        self._days_growing = 0
        self._type = "generic"
        self._status = "seed"
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need

    #Getter for growth attribute
    @property
    def get_growth(self): return self._growth

    @property
    def get_days_growing(self): return self._days_growing

    @property
    def get_type(self): return self._type

    @property
    def get_status(self): return self._status

    @property
    def get_growth_rate(self): return self._growth_rate

    @property
    def get_light_need(self): return self._light_need

    @property
    def get_water_need(self): return self._water_need

    def needs(self): return {"Light need": self._light_need, "Water need": self._water_need}

    def report(self): return {"Type": self._type, "Status": self._status, "Growth": self._growth,\
                              "Days growing": self._days_growing}

    def _update_status(self):
        for item in self.GROWTH_SCALE:
            if self._growth >= item[1]:
                self._status = item[0]
                break

    def grow(self, available_light, available_water):
        if available_light >= self._light_need and available_water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()


def auto_grow(crop, num_of_days):
    for _ in range(num_of_days):
        crop.grow(random.randint(1, 10), random.randint(1, 10))

def manual_grow(crop):
    available_water = 0
    available_light = 0
    while available_light not in range(1, 11):
        available_light = input("Please, input amount of available light(1-10): ")
    while available_water not in range(1, 11):
        available_water = input("Please, input amount of available water(1-10): ")
    crop.grow(available_light, available_water)


def display_menu():
    print "\n--------------------------\n1 - Manual Grow Crop\n2 - Automatically Grow Crop\n3 - Display Crop report\
    \n4 - Exit\n--------------------------\n"

def get_menu_choice():
    valid = False

    while not valid:
        choice = raw_input("Please, make your choice: ")
        if choice.isdigit() and int(choice) in (1, 2, 3, 4):
            valid = True
        else:
            print "Wrong input. Please select from 1 to 4."
    return int(choice)

def manage_crop(crop):
    exit_bool = False
    while not exit_bool:
        os.system('cls')
        display_menu()
        choice = get_menu_choice()
        if choice == 4:
            exit_bool = True
        elif choice == 1:
            manual_grow(crop)
        elif choice == 2:
            auto_grow(crop, 30)
        elif choice == 3:
            print crop.report()
            raw_input("Press Enter to continue...")

if __name__ == "__main__":
    wheat = Crop(1, 5, 5)
    rice = Crop(8, 8, 10)
    print "WHEAT:\nGrowth:", wheat.get_growth, "\nDays growing:", wheat.get_days_growing,\
            "\nType:", wheat.get_type, "\nStatus:", wheat.get_status, "\nLight need:", wheat.get_light_need,\
            "\nGrowth rate:", wheat.get_growth_rate, "\nWater need:", wheat.get_water_need
    print ""
    print "RICE:\nGrowth:", rice.get_growth, "\nDays growing:", rice.get_days_growing,\
            "\nType:", rice.get_type, "\nStatus:", rice.get_status, "\nLight need:", rice.get_light_need,\
            "\nGrowth rate:", rice.get_growth_rate, "\nWater need:", rice.get_water_need
    print wheat.needs()
    print wheat.report()
    raw_input("Press Enter to start Manage Crop")
    manage_crop(wheat)