import swapi


def q1():
    planets = swapi.get_all("planets").order_by("diameter")
    return planets


def q2():
    people = swapi.get_all("people").iter()

    pilot = set()

    for person in people:
        for sh in person.get_starships().iter():
            if sh:
                pilot.add(person)
                break
    return list(pilot)


def q3():
    vehicles = swapi.get_all("vehicles").iter()
    mas = [vi.max_atmosphering_speed for vi in vehicles]
    return mas

def q4():
    species = swapi.get_all("species").iter()
    for sp in species:
        if sp.name == "Dug":
            target = sp
            break

    films = target.get_films().iter()

    return films


def q5(person_id):
    person = swapi.get_person(person_id)
    species = person.get_species().iter()
    names = [sp.name for sp in species]
    return names