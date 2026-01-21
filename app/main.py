class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_istances_list = []
    for person in people:
        one_person = Person(person["name"], person["age"])
        if "wife" in person and person["wife"] is not None:
            one_person.wife = person["wife"]
        elif "husband" in person and person["husband"] is not None:
            one_person.husband = person["husband"]
        person_istances_list.append(one_person)

    for istanced_person in person_istances_list:
        if hasattr(istanced_person, "wife"):
            istanced_person.wife = Person.people[istanced_person.wife]
        elif hasattr(istanced_person, "husband"):
            istanced_person.husband = Person.people[istanced_person.husband]

    return person_istances_list
