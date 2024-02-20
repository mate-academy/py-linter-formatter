class Person:
    people = {}

    def __init__(self, name, age, spouse=None):
        self.name = name
        self.age = age
        self.spouse = None
        self.add_to_people()

        if spouse:
            self.add_spouse(spouse)

    def add_to_people(self):
        self.people[self.name] = self

    def add_spouse(self, spouse_name):
        spouse = self.people.get(spouse_name)
        if spouse:
            self.spouse = spouse
            spouse.spouse = self

def create_person_list(people):
    person_list = []
    for person_info in people:
        name = person_info['name']
        age = person_info['age']
        spouse = person_info.get('wife') or person_info.get('husband')
        person = Person(name, age, spouse)
        person_list.append(person)
    return person_list
