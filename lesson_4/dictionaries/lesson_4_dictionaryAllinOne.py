# coding=UTF-8
if __name__ == "__main__":

    import random
    solar_system = {
        'Mercury': 57.9,
        'Venus': 108.2,
        'Earth': 149.6,
        'Mars': 227.9,
        'Jupiter': 778.3,
        'Saturn': 1427,
        'Uranus': 2871,
        'Neptune': 4497.1,
        'Pluto': 5913
    }


    def print_planet_info(sorting):
        if sorting == '1':
            print "Without order:"
            for planet, distance in solar_system.iteritems():
                print "Planet {planet} is in {distance} millions km from the Sun".format(planet = planet, distance = distance)
        elif sorting == '2':
            print "Sorted by planets name:"
            for planet, distance in sorted(solar_system.iteritems()):
                print "Planet {planet} is in {distance} millions km from the Sun".format(planet = planet, distance = distance)
        elif sorting == '3':
            print "Sorted by distance:"
            for planet, distance in sorted(solar_system.iteritems(), key=lambda items: items[1]):
                print "Planet {planet} is in {distance} millions km from the Sun".format(planet = planet, distance = distance)
        elif sorting == '4':
            print "Random choice:"
            planet, distance = random.choice(solar_system.items())
            print "Planet {planet} is in {distance} millions km from the Sun".format(planet = planet, distance = distance)
        else:
            print "Choose correct option!"

    print "Please, choose order\n(1 - No order; 2 - sorted by planets name; 3 - sorted by distance from the Sun; 4 - random choice)\n"
    print_planet_info(raw_input())
    raw_input()