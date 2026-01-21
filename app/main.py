class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instanced_list = [Person(person["name"], person["age"])
                             for person in people]

    for instanced_person in person_instanced_list:
        for person in people:
            if instanced_person.name == person["name"]:
                if person.get("wife") is not None:
                    instanced_person.wife = Person.people[person["wife"]]
                elif person.get("husband") is not None:
                    instanced_person.husband = Person.people[person["husband"]]

    return person_instanced_list
